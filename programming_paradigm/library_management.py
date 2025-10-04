"""Book library for tracting books in a library"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self.list_books = []

    def add_book(self, book):
        self.list_books.append(book)

    def check_out_book(self, title):
        for book in self.list_books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                

    def return_book(self, title):
        for book in self.list_books:
            if book.title == title and book.is_checked_out():
                book.return_book()


    def list_available_books(self):

        for book in self.list_books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
        #print([book.title for book in self.list_books if not book.is_checked_out()])


    
# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that 
# tracks books in a library, focusing on classes, object instantiation, and method invocation.

# Your Task: library_management.py
# Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
# Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.