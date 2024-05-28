def solve_quadratic(a: int, b: int, c: int):
    quad = b ** 2 - 4 * a * c

    x = (-b + quad ** 0.5) / (2 * a)
    y = (-b - quad ** 0.5) / (2 * a)

    formatted_x = f"{x:.2f}"
    formatted_y = f"{y:.2f}"

    return f"x = {formatted_x}, y = {formatted_y}"


a = 3
b = 9
c = -42
result = solve_quadratic(a, b, c)
print(result)
