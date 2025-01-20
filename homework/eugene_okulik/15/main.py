import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

try:

    cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)", ('Alex', 'Sidorov', None))
    student_id = cursor.lastrowid  # Получаем ID студента


    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('Основы программирования', student_id))
    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('Введение в базы данных', student_id))


    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)", ('Gruppa2025', '2025-01-17', '2025-04-17'))
    group_id = cursor.lastrowid  # Получаем ID группы


    cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))


    cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ('Biologiya',))
    cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ('Himiya',))


    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Biologicheskie osnovy', 1))
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Ekologiya', 1))
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Organicheskaya himiya', 2))
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Neorganicheskaya himiya', 2))


    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (3, 1, student_id))
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (4, 2, student_id))
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (5, 3, student_id))
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (4, 4, student_id))


    cursor.execute("""
        SELECT
            s.name AS student_name,
            s.second_name AS student_second_name,
            g.title AS group_title,
            b.title AS book_title,
            m.value AS mark_value,
            l.title AS lesson_title,
            sub.title AS subject_title
        FROM
            students s
        LEFT JOIN
            `groups` g ON s.group_id = g.id
        LEFT JOIN
            books b ON b.taken_by_student_id = s.id
        LEFT JOIN
            marks m ON m.student_id = s.id
        LEFT JOIN
            lessons l ON m.lesson_id = l.id
        LEFT JOIN
            subjets sub ON l.subject_id = sub.id
        WHERE
            s.id = %s
    """, (student_id,))


    for row in cursor.fetchall():
        print(row)


    db.commit()

except mysql.Error as err:
    print(f"Ошибка: {err}")
    db.rollback()  # Откат изменений в случае ошибки

finally:
    cursor.close()
    db.close()
