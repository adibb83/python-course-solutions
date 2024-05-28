import unittest


import unittest

from HW1.solutions.data_from_html import extract_string_from_html
from HW1.solutions.quadratic import solve_quadratic


class MyTestCase(unittest.TestCase):
    def test_solve_quadratic(self):
        a = 2
        b = 5
        c = 3
        expected_result = "x = -1.00, y = -1.50"
        self.assertEqual(solve_quadratic(a, b, c), expected_result)


if __name__ == '__main__':
    unittest.main()
