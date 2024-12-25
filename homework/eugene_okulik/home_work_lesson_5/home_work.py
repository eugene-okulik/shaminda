person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

one_value = 'результат операции: 42'
new_one_value = one_value.index(':') + 2
number_str = one_value[new_one_value:]
if number_str.isdigit():
    number = int(number_str)
    result = number + 10
print(result)

two_value = 'результат операции: 514'
new_two_value = two_value.index(':') + 2
number_str_two = two_value[new_two_value:]
if number_str_two.isdigit():
    number_two = int(number_str_two)
    uspex = number_two + 10
print(uspex)

three_value = 'результат работы программы: 9'
new_three_value = three_value.index(':') + 2
number_str_three = three_value[new_three_value:]
if number_str_three.isdigit():
    number_three = int(number_str_three)
    result_two = number_three + 10
print(result_two)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)
subjects_str = ', '.join(subjects)

print(f'Students {students_str} study these subjects: {subjects_str}')

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
new_str = str(students[0])
new_str_two = str(students[1])
new_str_three = str(students[2])
subjects_one = str(subjects[0])
subjects_two = str(subjects[1])
subjects_three = str(subjects[2])

print(f'Students {new_str}, {new_str_two}, {new_str_three} study these subjects: {subjects_one}, {subjects_two}, {subjects_three} ')
#сначало сделал без джойнов , попробовал получилось, но запись длинная и не особо читаема






