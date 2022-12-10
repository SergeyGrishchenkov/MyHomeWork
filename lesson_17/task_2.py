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
        self.books.append(name)
        if not author in self.authors:
            self.authors.append(author)

    def group_by_author(self, author: Author):
        """returns a list of all books grouped by the specified author"""
        pass

    def group_by_year(self, year: int):
        """returns a list of all the books grouped by the specified year"""
        pass


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

    @property
    def amount_books(self):
        return self.__amount_books


def main():
    my_library = Library("The best for you!")


if __name__ == "__main__":
    main()
