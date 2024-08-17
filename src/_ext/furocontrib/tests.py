def construct_mermaid_html(content, options):
    """
    Constructs HTML content for different themes using provided text and options.

    :param content: List of text lines to be included in the HTML.
    :param options: Dictionary with options for different themes.
    :return: String of constructed HTML.
    """
    assert content, "Content should not be empty"

    text = '\n'.join(content)

    # Only dark configuration and HTML
    only_dark_theme = options.get("dark-theme", "dark")
    only_dark_html = f'<div class="mermaid only-dark">{text}</div>'

    # Only light configuration and HTML
    only_light_theme = options.get("light-theme", "light")
    only_light_html = f'<div class="mermaid only-light">{text}</div>'

    # Construct and return the HTML
    html = only_dark_html + only_light_html
    return html


import unittest


class TestMermaidHtmlConstruction(unittest.TestCase):

    def test_empty_content(self):
        with self.assertRaises(AssertionError):
            construct_mermaid_html([], {})

    def test_default_theme_options(self):
        content = ["Hello", "World"]
        html = construct_mermaid_html(content, {})
        self.assertIn('class="mermaid only-dark"', html)
        self.assertIn('class="mermaid only-light"', html)
        self.assertIn("Hello\nWorld", html)

    def test_custom_theme_options(self):
        content = ["Sample", "Text"]
        options = {"dark-theme": "dark-blue", "light-theme": "light-green"}
        html = construct_mermaid_html(content, options)
        self.assertIn('class="mermaid only-dark"', html)
        self.assertIn('class="mermaid only-light"', html)
        self.assertIn("Sample\nText", html)


if __name__ == '__main__':
    unittest.main()
