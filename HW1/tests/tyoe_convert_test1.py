import unittest

from HW1.solutions.type_conversion import convert_binary_to_decimal


class TestConvertBinaryToDecimal(unittest.TestCase):
    def test_convert_binary_to_decimal(self):
        binary_number = "1101"
        expected_decimal_value = 13
        actual_decimal_value = convert_binary_to_decimal(binary_number)
        self.assertEqual(actual_decimal_value, expected_decimal_value,
                         f"Expected decimal value {expected_decimal_value}, but got {actual_decimal_value}")


if __name__ == "__main__":
    unittest.main()
