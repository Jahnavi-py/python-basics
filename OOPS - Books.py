#Create a Book class and allow users to add and display details of books
class Books:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year: {self.year}")
       # print("-" * 30)
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, year):
        new_book = Books(title, author, genre, year)
        self.books.append(new_book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_details()
library = Library()
library.add_book("The Hound of Baskerville's", "Vampire Dariers", "Twlight", 1925)
library.add_book("1984", "Harry Potter", "Crypto Currency", "2000")
library.display_books()