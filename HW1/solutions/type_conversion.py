def convert_binary_to_decimal(binary_str):
    return int(binary_str, 2)


binary_number = "1101"
decimal_value = convert_binary_to_decimal(binary_number)
print(f"The decimal value of the binary number {binary_number} is: {decimal_value}")