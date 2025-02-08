import unittest
from typing import cast

from main import text_node_to_html_node
from src.main import text_to_textnodes
from textnode import TextNode, TextType
from htmlnode import LeafNode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        text_node = TextNode(text="Random text", text_type=TextType.TEXT)
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
            text="Random text", text_type=TextType.LINK, url="https://www.google.com"
        )
        expected_output = LeafNode(
            tag="a", value="Random text", props={"href": "https://www.google.com"}
        )
        self.assertEqual(text_node_to_html_node(text_node), expected_output)

    def test_text_node_to_html_node_images(self):
        text_node = TextNode(
            text="Random text",
            text_type=TextType.IMAGE,
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


class TestTextToTextNode(unittest.TestCase):
    def test_text_to_text_node_no_markdown(self):
        text = "Random text"
        self.assertEqual(text_to_textnodes(text), [TextNode("Random text", TextType.TEXT, )])

    def test_text_to_text_node_bold(self):
        text = "This text is **bold**."
        expected_output = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_node_italic(self):
        text = "This text is *italic*."
        expected_output = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_node_code(self):
        text = "This text is `code`."
        expected_output = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_node_image(self):
        text = "This text has an ![obvious image](https://www.image-link.com/) in it."
        expected_output = [
            TextNode("This text has an ", TextType.TEXT),
            TextNode("obvious image", TextType.IMAGE, "https://www.image-link.com/"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_node_link(self):
        text = "This text has a [link to wikipedia](https://www.wikipedia.notreal) in it."
        expected_output = [
            TextNode("This text has a ", TextType.TEXT),
            TextNode("link to wikipedia", TextType.LINK, "https://www.wikipedia.notreal"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)


if __name__ == "__main__":
    unittest.main()
