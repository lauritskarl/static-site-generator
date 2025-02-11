import unittest
from main import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes_no_markdown(self):
        text = "Random text"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode(
                    "Random text",
                    TextType.TEXT,
                )
            ],
        )

    def test_text_to_text_nodes_bold(self):
        text = "This text is **bold**."
        expected_output = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_nodes_italic(self):
        text = "This text is *italic*."
        expected_output = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_nodes_code(self):
        text = "This text is `code`."
        expected_output = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_nodes_image(self):
        text = "This text has an ![obvious image](https://www.image-link.com/) in it."
        expected_output = [
            TextNode("This text has an ", TextType.TEXT),
            TextNode("obvious image", TextType.IMAGE, "https://www.image-link.com/"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_text_to_text_nodes_link(self):
        text = (
            "This text has a [link to wikipedia](https://www.wikipedia.notreal) in it."
        )
        expected_output = [
            TextNode("This text has a ", TextType.TEXT),
            TextNode(
                "link to wikipedia", TextType.LINK, "https://www.wikipedia.notreal"
            ),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)


if __name__ == "__main__":
    unittest.main()
