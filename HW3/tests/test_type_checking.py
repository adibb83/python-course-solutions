import unittest

from HW3.solutions.type_checkin import type_check


class TestTypeCheck(unittest.TestCase):
    def test_type_check(self):
        @type_check
        def test_func(name: str, age: int, data: dict, other_info=None) -> str:
            other_info_str = ', Other Info : ' + str(other_info) if other_info else ''
            return f"Name: {name}, Age: {age}, Data: {data['key']}{other_info_str}"

        # Test with correct types
        self.assertEqual(test_func("John", 25, {"key": "value"}, "Extra Info"),
                         "Name: John, Age: 25, Data: value, Other Info : Extra Info")

        # Test with incorrect types
        with self.assertRaises(TypeError):
            test_func(123, 25, {"key": "value"}, "Extra Info")

        with self.assertRaises(TypeError):
            test_func("John", "25", {"key": "value"}, "Extra Info")

        with self.assertRaises(TypeError):
            test_func("John", 25, ["key", "value"], "Extra Info")



if __name__ == "__main__":
    unittest.main()
