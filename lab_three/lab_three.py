from typing import List

class Author:
    def __init__(self, name: str, biography: str):
        self.name = name
        self.biography = biography
        self.books: List['Book'] = []

    def add_book(self, book: 'Book'):
        self.books.append(book)

    def remove_book(self, book: 'Book'):
        self.books.remove(book)

    def __str__(self):
        return f"Author: {self.name}, Biography: {self.biography}"

class Book:
    def __init__(self, title: str, author: Author, pub_date: str, isbn: str, copies: int):
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.isbn = isbn
        self.copies = copies
        author.add_book(self)

    def reserve_copy(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False

    def return_copy(self):
        self.copies += 1

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author.name}, Copies: {self.copies}"

class TextBook(Book):
    def __init__(self, title: str, author: Author, pub_date: str, isbn: str, copies: int, subject: str, edition: int):
        super().__init__(title, author, pub_date, isbn, copies)
        self.subject = subject
        self.edition = edition

    def __str__(self):
        return f"TextBook: {self.title}, Subject: {self.subject}, Edition: {self.edition}"

class ReferenceBook(Book):
    def __init__(self, title: str, author: Author, pub_date: str, isbn: str, copies: int, category: str, is_reference: bool):
        super().__init__(title, author, pub_date, isbn, copies)
        self.category = category
        self.is_reference = is_reference

    def __str__(self):
        return f"ReferenceBook: {self.title}, Category: {self.category}, Reference: {self.is_reference}"

class Patron:
    def __init__(self, name: str, address: str, phone: str, email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.borrowed_books: List[Book] = []

    def borrow_book(self, book: Book):
        if book.reserve_copy():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_copy()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"Patron: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

if __name__ == "__main__":
 
    author1 = Author("J.K. Rowling", "British author best known for the Harry Potter series.")
    author2 = Author("George Orwell", "English novelist and essayist.")

    book1 = Book("Harry Potter and the Philosopher's Stone", author1, "1997-06-26", "9780747532743", 5)
    book2 = TextBook("1984", author2, "1949-06-08", "9780451524935", 3, "Dystopian", 1)
    book3 = ReferenceBook("Animal Farm", author2, "1945-08-17", "9780451526342", 2, "Political Satire", True)

    patron1 = Patron("Alice", "123 Main St", "555-1234", "alice@example.com")
    patron2 = Patron("Bob", "456 Elm St", "555-5678", "bob@example.com")

    patron1.borrow_book(book1)
    patron1.borrow_book(book2)

    success = patron2.borrow_book(book1)
    print(f"Patron2 successfully borrowed 'Harry Potter': {success}")

    print(patron1)
    print(patron2)
    print(book1)
    print(book2)
    print(book3)

    patron1.return_book(book1)
    print(patron1)
    print(book1)