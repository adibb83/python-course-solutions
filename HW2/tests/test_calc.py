import unittest

from HW2.solutions.calculater import simple_calc


class TestSimpleCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(simple_calc("add 2 and 3"), "The answer is 5")

    def test_subtract(self):
        self.assertEqual(simple_calc("subtract 5 from 10"), "The answer is 5")

    def test_multiply(self):
        self.assertEqual(simple_calc("multiply 2 by 3"), "The answer is 6")

    def test_divide(self):
        self.assertEqual(simple_calc("divide 10 by 2"), "The answer is 5")

    def test_divide_by_zero(self):
        self.assertEqual(simple_calc("divide 10 by 0"), "error")

    def test_help(self):
        self.assertEqual(simple_calc("help"), "help")

    def test_exit(self):
        self.assertEqual(simple_calc("exit"), "exit")

    def test_invalid_command(self):
        self.assertEqual(simple_calc("invalid command"), "error")


# Run the unit tests
unittest.main()
