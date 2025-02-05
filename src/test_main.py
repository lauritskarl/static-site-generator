import unittest
from typing import cast

from main import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        text_node = TextNode(text="Random text", text_type=TextType.NORMAL)
        expected_output = LeafNode(value="Random text")
        self.assertEqual(text_node_to_html_node(text_node), expected_output)

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode(text="Random text", text_type=TextType.BOLD)
        expected_output = LeafNode(tag="b", value="Random text")
        self.assertEqual(text_node_to_html_node(text_node), expected_output)

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode(text="Random text", text_type=TextType.ITALIC)
        expected_output = LeafNode(tag="i", value="Random text")
        self.assertEqual(text_node_to_html_node(text_node), expected_output)

    def test_text_node_to_html_node_code(self):
        text_node = TextNode(text="Random text", text_type=TextType.CODE)
        expected_output = LeafNode(tag="code", value="Random text")
        self.assertEqual(text_node_to_html_node(text_node), expected_output)

    def test_text_node_to_html_node_links(self):
        text_node = TextNode(
            text="Random text", text_type=TextType.LINKS, url="https://www.google.com"
        )
        expected_output = LeafNode(
            tag="a", value="Random text", props={"href": "https://www.google.com"}
        )
        self.assertEqual(text_node_to_html_node(text_node), expected_output)

    def test_text_node_to_html_node_images(self):
        text_node = TextNode(
            text="Random text",
            text_type=TextType.IMAGES,
            url="https://www.image_link.com",
        )
        expected_output = LeafNode(
            tag="img",
            value="",
            props={"src": "https://www.image_link.com", "alt": "Random text"},
        )
        self.assertEqual(text_node_to_html_node(text_node), expected_output)

    def test_text_node_to_html_node_invalid_text_type(self):
        with self.assertRaises(Exception):
            TextNode(text="Random text", text_type=cast(TextType, "OTHER"))


if __name__ == "__main__":
    unittest.main()
