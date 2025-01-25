import csv
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSW = os.getenv('DB_PASSW')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

base_path = os.path.abspath(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = os.path.join(homework_path, 'lesson_16', 'hw_data', 'data.csv')

try:
    if DB_PORT is not None:
        DB_PORT = int(DB_PORT)
    else:
        raise ValueError("DB_PORT не задан в .env файле")

    connection = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSW,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    cursor = connection.cursor()

    with open(csv_file_path, newline='') as csv_file:
        file_data = csv.reader(csv_file)
        header = next(file_data)
        missing_data = []

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            print(f"Проверка таблицы: {table_name}")

            cursor.execute(f"DESCRIBE `{table_name}`")
            columns = [column[0] for column in cursor.fetchall()]

            print(f"Заголовки из CSV: {header}")
            print(f"Столбцы в таблице '{table_name}': {columns}")

            missing_headers = [col for col in header if col not in columns]
            if missing_headers:
                print(f"Отсутствуют заголовки: {missing_headers} в таблице '{table_name}'.")
            else:
                for row in file_data:
                    conditions = ' AND '.join([f"{header[i]} = %s" for i in range(len(header))])
                    query = f"SELECT * FROM `{table_name}` WHERE {conditions}"
                    cursor.execute(query, row)

                    result = cursor.fetchone()
                    if result is None:
                        missing_data.append((table_name, row))
                    else:
                        matched_fields = {header[i]: row[i] for i in range(len(header)) if row[i] == str(result[i])}
                        print(f"Найдены совпадения в таблице '{table_name}': {matched_fields}")

                csv_file.seek(0)
                next(file_data)

        if missing_data:
            print("Отсутствующие данные в базе:")
            for table, data in missing_data:
                print(f"Таблица: {table}, Данные: {data}")
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
