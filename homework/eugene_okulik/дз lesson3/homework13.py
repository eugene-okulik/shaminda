import datetime
import re

file_path = '/Users/a123/shaminda/homework/eugene_okulik/hw_13/data.txt'




def read_file():
    with open(file_path, 'r') as file:
        for line in file.readlines():
            process_line(line.strip())


def process_line(line):
    parts = line.split(' - ')
    if len(parts) < 2:
        return

    number = parts[0].strip()

    date_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)', line)

    if not date_match:
        print(f"Ошибка: дата не найдена в строке '{line}'")
        return

    date_str = date_match.group(1)

    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    if number.startswith('1'):
        new_date = date_obj + datetime.timedelta(weeks=1)
        print(f"Номер {number}: {new_date}")

    elif number.startswith('2'):
        day_of_week = date_obj.strftime('%A')
        print(f"Номер {number}: {day_of_week}")

    elif number.startswith('3'):
        days_ago = (datetime.datetime.now() - date_obj).days
        print(f"Номер {number}: {days_ago} дней назад")


read_file()
