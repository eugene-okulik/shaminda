def sum_values():
    a = 100
    b = 50
    return a + b


result = sum_values()
print(result)


def difference():
    a = 100
    b = 50
    return a - b


result = difference()
print(result)


def product():
    a = 100
    b = 50
    return a * b


result = product()
print(result)


def calculate(x, y) -> int:
    result = (x - y) / (1 + x * y)
    return result


x = 1000
y = 500
result = calculate(x, y)
print(result)


a = 10.0
b = 20.0

arithmetic_mean = (a + b) / 2
geometric_mean = (a * b) ** 0.5

print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Среднее геометрическое: {geometric_mean}")


a = 3
b = 4
c = (a ** 2 + b ** 2) ** 0.5
area = 0.5 * a * b

print(f"Гипотенуза: {c}")
print(f"Площадь: {area}")
