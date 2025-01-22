import csv
import os
import mysql.connector
import creds


DB_USER = creds.DB_USER
DB_PASSW = creds.DB_PASSW
DB_HOST = creds.DB_HOST
DB_PORT = creds.DB_PORT
DB_NAME = creds.DB_NAME

print(f"DB_USER: {DB_USER}")
print(f"DB_PASSW: {DB_PASSW}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_PORT: {DB_PORT}")
print(f"DB_NAME: {DB_NAME}")

try:
    if DB_PORT is not None:
        DB_PORT = int(DB_PORT)
    else:
        raise ValueError("DB_PORT не задан в creds.py")

    connection = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSW,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    cursor = connection.cursor()


    csv_file_path = '/Users/a123/shaminda/homework/eugene_okulik/Lesson_16/hw_data/data.csv'
    with open(csv_file_path, newline='') as csv_file:
        file_data = csv.reader(csv_file)
        header = next(file_data)
        missing_data = []

        for row in file_data:
            query = "SELECT * FROM students WHERE name = %s AND second_name = %s"
            cursor.execute(query, (row[0], row[1]))

            if not cursor.fetchone():
                missing_data.append(row)

        # Выводим отсутствующие данные
        if missing_data:
            print("Отсутствующие данные в базе:")
            for data in missing_data:
                print(data)
        else:
            print("Все данные из файла присутствуют в базе.")

except mysql.connector.Error as err:
    print(f"Ошибка: {err}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
