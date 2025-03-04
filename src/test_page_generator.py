import unittest

from page_generator import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_valid_title(self):
        self.assertEqual(extract_title("# This is a title"), "This is a title")

    def test_invalid_title_no_hash(self):
        with self.assertRaises(ValueError):
            extract_title("This is not a title")

    def test_invalid_title_empty_string(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_valid_title_with_extra_spaces(self):
        self.assertEqual(
            extract_title("#    Title with spaces   "), "   Title with spaces   "
        )

    def test_valid_title_with_special_characters(self):
        self.assertEqual(
            extract_title("# Title with special characters!@#"),
            "Title with special characters!@#",
        )


if __name__ == "__main__":
    unittest.main()
