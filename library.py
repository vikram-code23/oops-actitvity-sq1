
# Library Management System


# Class 1: Book
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} [{status}]"


# Class 2: Library
class Library:

    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added successfully.")

    # Borrow a book
    def borrow(self, title):

        for book in self.books:

            if book.title == title:

                if book.available:
                    book.available = False
                    print(f"'{title}' borrowed successfully.")

                else:
                    print(f"Sorry, '{title}' is already borrowed.")

                return

        print(f"No book titled '{title}'.")

    # Return a book
    def return_book(self, title):

        for book in self.books:

            if book.title == title:

                if not book.available:
                    book.available = True
                    print(f"'{title}' returned successfully.")

                else:
                    print(f"'{title}' was not borrowed.")

                return

        print(f"No book titled '{title}'.")

    # Display all books
    def show_books(self):

        for book in self.books:
            print(book)


# Main Program

# Create Library object
library = Library()

# Create Book objects
book1 = Book("Python 101", "Rao")
book2 = Book("Java Basics", "John")
book3 = Book("Linux Essentials", "David")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books
print("\n--- Library Books ---")
library.show_books()

# Borrow a book
print("\n--- Borrow Book ---")
library.borrow("Python 101")

# Try borrowing the same book again
print("\n--- Borrow Again ---")
library.borrow("Python 101")

# Return the book
print("\n--- Return Book ---")
library.return_book("Python 101")

# Display updated book status
print("\n--- Final Book List ---")
library.show_books()
