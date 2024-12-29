def process_value(value):
    new_one_value = value.index(':') + 2
    number_str = value[new_one_value:]

    if number_str.isdigit():
        number = int(number_str)
        return number + 10
    return None

one_value = 'результат операции: 42'
result = process_value(one_value)

if result is not None:
    print(result)

def process_value_two(value):
    new_two_value = value.index(':') + 2
    number_str_two = value[new_two_value:]

    if number_str_two.isdigit():
        number = int(number_str_two)
        return number + 10
    return None

two_value = 'результат операции: 514'
result = process_value_two(two_value)
if result is not None:
    print(result)

def process_value_three(value):
    new_three_value = value.index(':') + 2
    number_str_three = value[new_three_value:]

    if number_str_three.isdigit():
        number = int(number_str_three)
        return number + 10
    return None

three_value = 'результат работы программы: 9'
result = process_value_three(three_value)
if result is not None:
    print(result)
