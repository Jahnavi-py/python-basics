#Implement a Library class to manage book borrowing and returning.
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book : '{book.title}' added to the library.\n")
    def list_books(self):
        print("BOOKS AVAILABLE IN THE LIBRARY :\n")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"'{book.title}' by {book.author} - {status}\n")
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"Sorry, we don't have a book titled '{title}'.\n")
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Sorry, we don't have a record of a borrowed book titled '{title}'.\n")
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You've borrowed '{self.title}' by {self.author}.\n")
        else:
            print(f"'{self.title}' is already borrowed.")
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You've returned '{self.title}' by {self.author}.\n")
        else:
            print(f"'{self.title}' was not borrowed.\n")
library = Library()
book1 = Book("The Hound of Baskerville", "Sherlock Holmes")
book2 = Book("Vampire Diaries", "L.J.Smith")
library.add_book(book1)
library.add_book(book2)
library.list_books()
library.borrow_book("1984")
library.borrow_book("The Hound of Baskerville")
library.return_book("The Hound of Baskerville")