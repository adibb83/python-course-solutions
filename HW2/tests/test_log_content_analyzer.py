import unittest

from HW2.solutions.log_content_analyzer import analyze_log_content


class TestAnalyzeLogContent(unittest.TestCase):
    def test_empty_log(self):
        result = analyze_log_content('')
        self.assertEqual(result, {'Error': 0, 'Warning': 0, 'Info': 0})

    def test_multiple_words_log(self):
        result = analyze_log_content('Error Warning Info Error Info why so serious? ')
        self.assertEqual(result, {'Error': 2, 'Warning': 1, 'Info': 2})

    def test_case_insensitive(self):
        result = analyze_log_content('error WARNING info')
        self.assertEqual(result, {'Error': 1, 'Warning': 1, 'Info': 1})


if __name__ == '__main__':
    unittest.main()

