def type_check(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for i, arg in enumerate(args):
            arg_name = list(annotations.keys())[i]
            is_return = arg_name == 'return'
            if is_return:
                continue
            expected_type = annotations[arg_name]
            if not isinstance(arg, expected_type):
                raise TypeError(f'Argument {arg_name} is not of expected type {expected_type.__name__}')

        for kwarg, value in kwargs.items():
            expected_type = annotations[kwarg]
            if not isinstance(value, expected_type):
                raise TypeError(f'Argument {kwarg} is not of expected type {expected_type.__name__}')

        return func(*args, **kwargs)

    return wrapper


@type_check
def format_data(name: str, age: int, data: dict, other_info=None) -> str:
    other_info_str = ', Other Info : ' + str(other_info) if other_info else ''
    return f"Name: {name}, Age: {age}, Data: {data['key']}{other_info_str}"


# Test the function with correct types
print(format_data("Alice", 30, {"key": "value"}, 1234))

# Test the function with incorrect types
print(format_data("Alice", "thirty", {"key": "value"}))
