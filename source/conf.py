# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

if os.name == 'nt':
    os.environ["PATH"] += os.pathsep + os.path.join(os.environ["CONDA_PREFIX"],
                                                    "Library/bin/dot")

# -- CUSTOM: Retrieve CHANGELOG on top level for each rebuild

import shutil

shutil.copyfile("../CHANGELOG.rst", "./CHANGELOG.rst")

# -- CUSTOM: Retrieve developer-prime repo for source code examples

import git
import os

HERE = os.getcwd()
TEMP = "tmp"
DEST = os.path.join(HERE, TEMP)
REPO = "https://github.com/tudat-team/developer-primer"
TAG = "0.0.1"

if os.path.exists(DEST):
    shutil.rmtree(DEST)

os.mkdir(DEST)

git.Git(DEST).clone(REPO, branch=TAG)
# exclude_patterns = ["./tmp/"]
# print(exclude_patterns)

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- CUSTOM: Latex Customization

# latex_elements = {
#     "maketitle": "\\input{cover.tex}"
# }

# -- CUSTOM: FontAwesome Inline Icons https://sphinx-panels.readthedocs.io/en/latest/#inline-icons
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"]
panels_add_fontawesome_latex = True

# -- CUSTOM: sphinx.ext.todo
todo_include_todos = True

# -- Project information -----------------------------------------------------

project = 'Tudat Developer'
copyright = '2021, Tudat Space'

# Custom: Make authors automatically retrieve, in order of Rever's ordering,
#    and added as documentation authors.
import re

with open("../AUTHORS", "r") as f:
    author = ', '.join(list(re.findall(r"^\*\s(.*)", f.read(), re.MULTILINE)))

# The full version, including alpha/beta/rc tags
release = '0.0.11'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.bibtex",
    'sphinx_panels',
    "sphinx.ext.graphviz",
    # 'sphinx_toolbox.shields',
    'sphinx.ext.todo',
    "sphinx.ext.autosectionlabel"
]

graphviz_output_format = 'svg'  # manual: as apposed to .png by default

# extension specific variables
bibtex_bibfiles = ['primer/primer.bib']
bibtex_default_style = 'unsrt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "furo"
# html_theme = "insipid"
html_title = f'Tudat Developer'

if html_theme == "insipid":
    html_add_permalinks = '\N{SECTION SIGN}'
    html_context = {'display_github': True, 'github_user': 'sphinx-themes',
                    'github_repo': 'sphinx-themes.org',
                    'conf_py_path': '/sample-docs/', 'commit': 'master'}
    html_copy_source = False

# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "_static/cover.png"
