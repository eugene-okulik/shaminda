def finish_me(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('finished')
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')


def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            func(*args, **kwargs)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


def operation_manager(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        else:
            operation = '*'  # На случай, если одно из чисел отрицательное

        return func(first, second, operation)

    return wrapper


@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second if second != 0 else 'Ошибка: деление на ноль'
    elif operation == '*':
        return first * second


# Запрос чисел у пользователя
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result = calc(num1, num2)
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: введите корректные числа.")


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {line.split()[0]: int(line.split()[1][:-1]) for line in PRICE_LIST.strip().split('\n')}
print(price_dict)
