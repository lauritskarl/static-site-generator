import unittest
from main import block_to_block_type


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
