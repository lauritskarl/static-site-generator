import unittest
from main import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_no_markdown(self):
        markdown = ""
        self.assertEqual(markdown_to_blocks(markdown), [])

    def test_markdown_to_blocks_empty_lines(self):
        markdown = "First line of text\n\n\nAnother line\n\n\n"
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "First line of text",
                "Another line",
            ],
        )

    def test_markdown_to_blocks_many_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )


if __name__ == "__main__":
    unittest.main()
