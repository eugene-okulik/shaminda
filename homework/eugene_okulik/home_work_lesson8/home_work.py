import random
import sys

sys.set_int_max_str_digits(1000000)

user_input = int(input('Какая у тебя зарплата?: '))
bonus = random.choice([True, False])

def user_count_bonus(user_input, bonus):
    if user_input > 0:
        if bonus == True:
            count = random.randint(100, 1000)
            total_salary = user_input + count
            return f'Итоговая зарплата с бонусом: ${total_salary}'
        else:
            return f'Итоговая зарплата: ${user_input}'
    else:
        return "Зарплата должна быть больше 0."

result = user_count_bonus(user_input, bonus)
print(result)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()

fifth_number = None
two_hundredth_number = None
thousandth_number = None
hundred_thousandth_number = None

for index, value in enumerate(fib_gen):
    if index == 4:
        fifth_number = value
    if index == 199:
        two_hundredth_number = value
    if index == 999:
        thousandth_number = value
    if index == 99999:
        hundred_thousandth_number = value
        break  # на этом задании у меня сгорел комп и не только он ...


print(f'Пятое число Фибоначчи: {fifth_number}')
print(f'Двухсотое число Фибоначчи: {two_hundredth_number}')
print(f'Тысячное число Фибоначчи: {thousandth_number}')
print(f'Стотысячное число Фибоначчи: {hundred_thousandth_number}')
