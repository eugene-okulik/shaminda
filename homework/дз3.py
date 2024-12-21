def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)
data = [5,9]
result = arithmetic_mean(data)
print(result)

## как посчитать среднее геометрическое не могу дойти ,
## нам надо произвидение чисел , кол - во чисел их 2 , и извлечь корень 2 из произведение
## все до извлечение корня знаю как дальше не могу понять
## оставлю такую запись но мне кажется это не правильно
def geometric_mean(numbers):
    return sum(numbers) * len(numbers)
data = [5,9]
result = geometric_mean(data)
print(result)