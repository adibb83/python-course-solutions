from typing import List


def simple_calc(user_input: str) -> str:
    operation_options = ["add", "subtract", "multiply", "divide", "help", "exit"]
    word_array = user_input.split()

    def string_exists(target: str, string_array: list[str]) -> bool:
        return target in string_array

    def get_user_numbers(user_input: list[str]) -> list[int]:
        extracted_numbers: list[int] = []
        for s in user_input:
            if s.isdigit():
                extracted_numbers.append(int(s))
        return extracted_numbers

    def error_message():
        print("invalid input try please try again!! For example: multiply 2 by 5")

    def result_message(result: float) -> str:
        return f"The answer is {result}"

    if word_array and string_exists(word_array[0], operation_options):
        numbers = get_user_numbers(word_array)
        match word_array[0].lower():
            case "add":
                return result_message(numbers[0] + numbers[1])
            case "subtract":
                return result_message(numbers[0] - numbers[1])
            case "multiply":
                return result_message(numbers[0] * numbers[1])
            case "divide":
                if numbers[0] == 0 or numbers[1] == 0:
                    error_message()
                    return 'error'
                else:
                    return result_message(numbers[0] // numbers[1])
            case "help":
                print("write an arithmetic exercise. Use only words. For example: multiply 2 by 5")
                return 'help'
            case "exit":
                return "exit"
    else:
        error_message()
        return 'error'


print("write an arithmetic exercise. Use only words. For example: multiply 2 by 5")
result = ""
while not result == "exit":
    user_input = input()
    result = simple_calc(user_input)
    if not result == 'error' and not result == 'help':
        print(result)
