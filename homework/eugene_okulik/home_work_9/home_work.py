import datetime


dana_data = "Jan 15, 2023 - 12:05:33"
# Преобразуем строку в объект datetime
data_in_python_two = datetime.datetime.strptime(dana_data, '%b %d, %Y - %H:%M:%S')


full_month_name = data_in_python_two.strftime('%B')
print(full_month_name)


formatted_date = data_in_python_two.strftime('%d.%m.%Y, %H:%M')
print(formatted_date)


temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]


high_temperatures = list(filter(lambda x: x >= 28, temperatures))
print(high_temperatures)


max_temp = max(high_temperatures)
min_temp = min(high_temperatures)

print(max_temp)
print(min_temp)


average_temp = sum(high_temperatures) / len(high_temperatures)
print(round(average_temp, 1))
