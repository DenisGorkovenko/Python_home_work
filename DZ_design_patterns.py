class Book:
    def __init__(self, book_id: str, title: str, author: str, year_public: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year_public = year_public

    def __str__(self):
        return f'{self.title}, {self.author}, {self.year_public}'


class Library:
    def __init__(self):
        self._storage = {}

    def __str__(self):
        result = []
        for key, value in self._storage.items():
            result.append(f'{str(value[0])}')
        return str(result)

    def add_book(self, book_id, title, author, year_public):
        new_book = Book(book_id, title, author, year_public)
        self._storage[book_id] = [new_book]

    def update_book(self, book_id, up_book):
        self._storage.update({book_id: [up_book]})

    def del_book(self, book_id):
        del self._storage[book_id]


lib = Library()

lib.add_book('b01', 'War and Peace', 'Leo Tolstoy', '1869')
lib.add_book('b02', 'The Idiot', 'Fyodor Dostoyevsky', '1868')
lib.add_book('b03', 'The Captains Daughter', 'Alexander Pushkin', '1836')

print(lib)

lib.del_book('b03')
print(lib)

lib.update_book('b02', 'What Is to Be Done?, Nikolai Chernyshevsky, 1863')
print(lib)
