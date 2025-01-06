class Book:
    material_of_pages = 'бумага'
    presence_of_text = True

    def __init__(self, title, author, num_pages, isbn=None, reserved=False):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (f'Название: {self.title}, Автор: {self.author}, '
                f'страниц: {self.num_pages}, '
                f'материал: {self.material_of_pages}, {reserved_status}'.strip())


class SchollBook(Book):
    def __str__(self):
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (f'Название: {self.title}, Автор: {self.author}, '
                f'страниц: {self.num_pages}, '
                f'материал: {self.material_of_pages}, {reserved_status}'.strip())
        super().__init__(title, author, num_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.is_mission = is_mission

    def __str__(self):
        is_mission_status = 'есть дз' if self.is_mission else 'нет дз'
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (f'Название: {self.title}, Автор: {self.author}, '
                f'страниц: {self.num_pages}, предмет: {self.subject}, '
                f'класс: {self.school_class}, {reserved_status}, '
                f'{is_mission_status}'.strip())


book_one = Book('Война и мир', 'Толстой', 1200)
book_two = Book('Преступление и наказание', 'Гоголь', 500, reserved=True)
book_three = Book("1984", "Джордж Оруэлл", 328)
book_four = Book("Моби Дик", "Герман Мелвилл", 635)
book_five = Book("Убить пересмешника", "Харпер Ли", 281)

scholl_book = SchollBook(
    'Алгебра', 'Иванов', 200, reserved=True,
    subject='Математика', school_class='9', is_mission=True
)
scholl_book1 = SchollBook(
    'Английский', 'Сидоров', 400, reserved=False,
    subject='Английский', school_class='10'
)

books = [
    book_one, book_two, book_three, book_four,
    book_five, scholl_book, scholl_book1
]

for book in books:
    print(book)
