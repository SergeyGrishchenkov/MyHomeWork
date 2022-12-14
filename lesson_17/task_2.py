# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books

class Author:
    def __init__(self, name: str, country: str, birthday: str, books: list = []):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __eq__(self, other):
        if self.name == other.name and self.country == other.country and self.birthday == other.birthday:
            return True
        else:
            return False

    def is_member(self, set_books: list):
        for item in set_books:
            if self == item:
                return True
            else:
                return False

class Library:
    __amount_books = 0

    def __init__(self, name: str, books: list = [], authors: list = []):
        self.name = name
        self.books = books
        self.authors = authors

    @property
    def amount_books(self):
        return self.__amount_books

    def new_book(self, name: str, year: int, author: Author):
        """returns an instance of Book class and adds the book to the books list for the current library"""
        new_book = Book(name, year, author)
        self.books.append(new_book)
        self.__amount_books += 1
        if not author in self.authors:
            self.authors.append(author)
            print(f'{author.__dict__} added')


    def group_by_author(self, author: Author):
        """returns a list of all books grouped by the specified author"""
        l = []
        for b in self.books:
            if author == b.author:
                l.append(b)
        return l

    def group_by_year(self, year: int):
        l = []
        for b in self.books:
            if year == b.year:
                l.append(b)
        return l


class Book:
    __amount_books = 0

    def __new__(cls, *args, **kwargs):
        cls.__amount_books += 1
        instance = super().__new__(cls)
        return instance

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        self.__amount_books += 1

    @property
    def amount_books(self):
        return self.__amount_books


def main():
    my_library = Library("The best for you!")
    my_library.new_book("Love Story 1", 2020, Author("Vika", "Ukraine", "2000-01-01", ))
    my_library.new_book("Love Story 2", 2021, Author("Taras", "Ukraine", "1990-01-01", ))
    my_library.new_book("Love Story 3", 2015, Author("Vika", "Ukraine", "2000-01-01", ))
    my_library.new_book("Love Story 4", 2021, Author("Vika", "Ukraine", "2000-01-01", ))
    my_library.new_book("Love Story 5", 2015, Author("Taras", "Ukraine", "1990-01-01", ))
    my_library.new_book("Love Story 6", 2020, Author("Taras", "Ukraine", "1990-01-01", ))

    author_list = my_library.group_by_author(Author("Vika", "Ukraine", "2000-01-01", ))
    print(author_list)
    print('*' * 20)
    year_list = my_library.group_by_year(2020)
    print(year_list)
    print('*'*20)
    print(f'Amount of books in Library: {my_library.amount_books}')


if __name__ == "__main__":
    main()
