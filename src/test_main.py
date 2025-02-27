import unittest

from main import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title"
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_extract_first_title_if_multiple_titles(self):
        markdown = "# This is a title\n# This is a second title"
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_extract_title_if_title_not_in_first_line(self):
        markdown = "This is just some text\n# This is the title on the second line"
        self.assertEqual(extract_title(markdown), "This is the title on the second line")

if __name__ == "__main__":
    unittest.main()
