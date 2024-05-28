import unittest

from HW1.solutions.data_from_html import extract_string_from_html


# Provide the missing imports


class TestExtractPID(unittest.TestCase):

    def test_extract_pid(self):
        html_text = "<html><head><title>Why So Serious</title></head><body></body></html>"
        expected_output = "Why So Serious"
        actual_result = extract_string_from_html(html_text)
        self.assertEqual(actual_result, expected_output)


if __name__ == '__main__':
    unittest.main()