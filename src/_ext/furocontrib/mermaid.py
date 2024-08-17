from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
from sphinx.application import Sphinx
import logging
import codecs
from sphinx.util.i18n import search_image_for_language
import json
import warnings
from sphinx.util.fileutil import copy_asset
import os


# Function to validate theme configuration
def theme_spec(argument):
    return directives.choice(
        argument,
        ("default", "neutral", "dark", "forest", "base", "light"))


# from bs4 import BeautifulSoup as bs
from lxml import etree, html


# Mermaid directive class
def parse_config(config, config_name):
    """Parse the configuration JSON and handle errors."""
    if isinstance(config, dict):
        return config
    try:
        return json.loads(config)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid '{config_name}' option")


def update_theme_option(config, theme_option, theme_type):
    """Update theme in configuration based on provided theme option."""
    if theme_option:
        if 'theme' in config:
            warnings.warn(
                f"{theme_type.capitalize()} theme specified in both '{theme_type}-theme' and '{theme_type}-config'")
        config['theme'] = theme_option


import html as stdlib_html
import re

import uuid


def generate_html(config, text, class_name):
    # Regular expression to find JSON enclosed in %% { ... } %%
    pattern = r'%%\s*({.*?})\s*%%'

    # Search for JSON configuration in the text
    match = re.search(pattern, text)
    json_config = {}

    if match:
        try:
            json_config_text = match.group(1)
            json_config = json.loads(json_config_text)
            # Remove the found JSON configuration from the text
            text = re.sub(pattern, '', text)
        except json.JSONDecodeError:
            print("Invalid JSON in text")

    # Merge the extracted configuration with the provided config
    merged_config = {**config, **json_config}
    merged_config_str = json.dumps(merged_config)
    text = (('%%{\n'
             '   init : ') + merged_config_str +
            '\n}%%' + text)
    # print(text)
    # Generate a unique ID for each Mermaid diagram
    unique_id = str(uuid.uuid4())
    return f'<div class="mermaid {class_name}" id={unique_id}>{text}</div>'


class MermaidDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    option_spec = {
        "light-theme": theme_spec,
        "dark-theme": theme_spec,
        "dark-config": directives.unchanged,
        "light-config": directives.unchanged,
    }

    def get_mm_code(self):
        if self.arguments:
            # try to load mermaid code from an external file
            document = self.state.document
            if self.content:
                return [
                    document.reporter.warning(
                        "Mermaid directive cannot have both content and "
                        "a filename argument",
                        line=self.lineno,
                    )
                ]
            env = self.state.document.settings.env
            argument = search_image_for_language(self.arguments[0], env)
            rel_filename, filename = env.relfn2path(argument)
            env.note_dependency(rel_filename)
            try:
                with codecs.open(filename, "r", "utf-8") as fp:
                    mmcode = fp.read()
            except OSError:
                return [
                    document.reporter.warning(
                        "External Mermaid file %r not found or reading "
                        "it failed" % filename,
                        line=self.lineno,
                    )
                ]
        else:
            # inline mermaid code
            mmcode = "\n".join(self.content)
        return mmcode

    def run(self):
        self.state.document.settings.env.note_dependency("./mermaid.css")
        text = self.get_mm_code()

        # Parse and validate configurations
        only_dark_config = parse_config(
            self.options.get("dark-config", {}),
            "dark-config")
        only_light_config = parse_config(
            self.options.get("light-config", {}),
            "light-config")

        # Update configurations with theme options
        update_theme_option(
            only_dark_config,
            self.options.get("dark-theme"),
            "dark")
        update_theme_option(
            only_light_config,
            self.options.get("light-theme"),
            "light")

        # Set default themes if not provided
        only_dark_config.setdefault("theme", "dark")
        only_light_config.setdefault("theme", "light")

        # Generate HTML content
        only_dark_html = generate_html(
            only_dark_config, text,
            "_only-dark")
        only_light_html = generate_html(
            only_light_config, text,
            "_only-light")

        # Construct the HTML for the Mermaid graph
        raw_html = f"<div class='mermaid-container'>\n{only_dark_html}{only_light_html}\n</div>"
        # print(raw_html)
        return [nodes.raw('', raw_html, format='html')]


class mermaid(nodes.General, nodes.Inline, nodes.Element):
    pass


def copy_asset_files(app, exc, asset_files):
    """
    Copies asset files to the output directory if the build succeeded.

    :param app: The Sphinx application object.
    :param exc: Exception object, None if the build succeeded.
    :param asset_files: List of asset file paths to be copied.
    """
    if exc is not None:  # build failed, don't copy
        return

    output_dir = os.path.join(app.outdir, '_static')
    for path in asset_files:
        try:
            copy_asset(path, output_dir)
        except Exception as e:
            app.warn(f"Error copying {path}: {e}")


# Main setup function for the Sphinx extension
def setup(app):
    # Add configurations
    app.add_config_value("mermaid_version", "latest", "env")
    app.add_js_file(
        "https://unpkg.com/mermaid/dist/mermaid.min.js")  # Add Mermaid JS

    # Add CSS for Mermaid
    app.add_css_file("furocontrib__mermaid.css")  # Add Mermaid CSS

    # Add JavaScript for rendering Mermaid diagrams
    filepath_js = os.path.join(
        os.path.dirname(__file__),
        "furocontrib__mermaid.js")

    with open(filepath_js, 'r') as f:
        js = f.read()
        app.add_js_file(None, body=js)

    # Add Mermaid directive
    app.add_directive("mermaid", MermaidDirective)

    # Asset files to be copied
    asset_files = [
        os.path.join(os.path.dirname(__file__), "furocontrib__mermaid.css"),
        # Add other asset file paths here
    ]

    # Connect the 'build-finished' event to the copy_asset_files function
    app.connect('build-finished',
                lambda app, exc: copy_asset_files(app, exc, asset_files))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
