import unittest

from main import markdown_to_html_node
from htmlnode import HTMLNode


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_node_paragraph(self):
        markdown = "This is a paragraph"
        expected_output = HTMLNode(tag="div")
        self.assertEqual(markdown_to_html_node(markdown), expected_output)
        pass

    def test_markdown_to_html_node_heading(self):
        markdown = "# This is a heading"
        expected_output = HTMLNode(tag="div")
        self.assertEqual(markdown_to_html_node(markdown), expected_output)
        pass

    def test_markdown_to_html_node_code(self):
        # TODO: Also test multiple lines.
        markdown = "```here is some code```"
        expected_output = HTMLNode(tag="div")
        self.assertEqual(markdown_to_html_node(markdown), expected_output)
        pass

    def test_markdown_to_html_node_quote(self):
        # TODO: Also test multiple lines.
        markdown = ">This is a quote"
        expected_output = HTMLNode(tag="div")
        self.assertEqual(markdown_to_html_node(markdown), expected_output)
        pass

    def test_markdown_to_html_node_unordered_list(self):
        # TODO: Also test multiple lines.
        markdown = "* This is an unordered list item"
        expected_output = HTMLNode(tag="div")
        self.assertEqual(markdown_to_html_node(markdown), expected_output)
        pass

    def test_markdown_to_html_node_ordered_list(self):
        # TODO: Also test multiple lines.
        markdown = "1. This is an ordered list item"
        expected_output = HTMLNode(tag="div")
        self.assertEqual(markdown_to_html_node(markdown), expected_output)
        pass

    def test_markdown_to_html_node_lots_of_markdown(self):
        markdown = (
            "This is a paragraph"
            "# This is a heading"
            "```here is some code```"
            ">This is a quote"
            "* This is an unordered list item"
            "1. This is an ordered list item"
        )
        nodes = [HTMLNode(), HTMLNode(), HTMLNode(), HTMLNode(), HTMLNode(), HTMLNode()]
        expected_output = HTMLNode(tag="div", children=nodes)
        self.assertEqual(markdown_to_html_node(markdown), expected_output)

    # TODO: also test empty lines between, empty space to left/right, etc


if __name__ == "__main__":
    unittest.main()
