import unittest
from typing import cast

from main import text_node_to_html_node
from src.main import text_to_textnodes, markdown_to_blocks, block_to_block_type
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


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_no_markdown(self):
        markdown = ""
        self.assertEqual(markdown_to_blocks(markdown), [])

    def test_markdown_to_blocks_empty_lines(self):
        markdown = "First line of text\n\n\nAnother line\n\n\n"
        self.assertEqual(markdown_to_blocks(markdown), [
            "First line of text",
            "Another line",
        ])

    def test_markdown_to_blocks_many_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(markdown_to_blocks(markdown), [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ])


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        block = "A simple paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_heading(self):
        block = "# A valid heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_block_to_block_type_max_heading(self):
        block = "###### A valid heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_block_to_block_type_invalid_heading(self):
        block = "####### An invalid heading"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_code(self):
        block = "```A valid code block```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_block_to_block_type_invalid_code(self):
        block = "``An invalid code block```"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_quote(self):
        block = ">A valid quote"
        self.assertEqual(block_to_block_type(block), "quote")

    def test_block_to_block_type_multiline_quote(self):
        block = ">A valid quote\n>Another valid quote"
        self.assertEqual(block_to_block_type(block), "quote")

    def test_block_to_block_type_invalid_multiline_quote(self):
        block = ">A valid quote line\nInvalid quote line making quote invalid"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_unordered_list_star(self):
        block = "* A valid unordered list item"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_to_block_type_unordered_list_dash(self):
        block = "- A valid unordered list item"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_to_block_type_multiline_unordered_list_star(self):
        block = "* A valid unordered list item\n* Another valid unordered list item"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_to_block_type_multiline_unordered_list_dash(self):
        block = "- A valid unordered list item\n- Another valid unordered list item"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_to_block_type_multiline_unordered_list_star_and_dash(self):
        block = "- A valid unordered list item\n* Another valid unordered list item"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_to_block_type_invalid_unordered_list_star(self):
        block = "*An invalid unordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_invalid_unordered_list_dash(self):
        block = "-An invalid unordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_invalid_multiline_unordered_list_star(self):
        block = "* A valid unordered list item\n*An invalid unordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_invalid_multiline_unordered_list_dash(self):
        block = "- A valid unordered list item\n-An invalid unordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_invalid_multiline_unordered_list_star_and_dash(self):
        block = "- A valid unordered list item\n*An invalid unordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_ordered_list(self):
        block = "1. A valid ordered list item"
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_block_to_block_type_ordered_list_large_number(self):
        block = "8923984. A valid ordered list item"
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_block_to_block_type_invalid_ordered_list_no_space(self):
        block = "1.An invalid ordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_invalid_ordered_list_no_period(self):
        block = "1 An invalid ordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_invalid_ordered_list_not_int(self):
        block = "x. An invalid ordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_multiline_ordered_list(self):
        block = "1. A valid ordered list item\n2. Another valid ordered list item"
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_block_to_block_type_invalid_multiline_ordered_list(self):
        block = "1. A valid ordered list item\n2.An invalid ordered list item"
        self.assertEqual(block_to_block_type(block), "paragraph")


if __name__ == "__main__":
    unittest.main()
