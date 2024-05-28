import unittest


import unittest

from HW1.solutions.data_from_html import extract_string_from_html


class MyTestCase(unittest.TestCase):
    def test_returns_string(self):
        html_text = "<html><head><title>Why So Serious</title></head><body></body></html>"

        result = extract_string_from_html(html_text)

        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
