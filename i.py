class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class LibraryMember:
    def title_search(self, title):
        raise NotImplementedError("title_search method not implemented.")
    
    def author_search(self, author):
        raise NotImplementedError("author_search method not implemented.")
    
    def genre_search(self, genre):
        raise NotImplementedError("genre_search method not implemented.")
    
    def borrow_book(self, book, user):
        raise NotImplementedError("borrow_book method not implemented")
    
    def return_book(self, book, user):
        raise NotImplementedError("return_book method not implemented.")
    
class LibraryStaff:
    def add_book(self, book):
        raise NotImplementedError("add_book method not implemented.")
    
    def remove_book(self, book):
        raise NotImplementedError("remove_book method not implemented.")
    
    def generate_borrowings_report(self):
        raise NotImplementedError("generate_borrowings_report method not implemented.")
    
    def generate_overdue_books_report(self):
        raise NotImplementedError("generate_overdue_books_report method not implemented.")
    
    def generate_popularity_report(self):
        raise NotImplementedError("generate_popularity_report method not implemented.")
    
class Guest(LibraryMember):
    def title_search(self, title):
        print(f"Searching for book with title: {title}")
    
    def author_search(self, author):
        print(f"Searching for book with author: {author}")
    
    def genre_search(self, genre):
        print(f"Searching for book with genre: {genre}")
    
    def borrow_book(self, book, user):
        print(f"User: {user} borrowing book: {book.title}")
    
    def return_book(self, book, user):
        print(f"User: {user} returning book: {book.title}")

class Librarian(LibraryMember, LibraryStaff):
    def title_search(self, title):
        print(f"Searching for book with title: {title}")
    
    def author_search(self, author):
        print(f"Searching for book with author: {author}")
    
    def genre_search(self, genre):
        print(f"Searching for book with genre: {genre}")
    
    def borrow_book(self, book, user):
        print(f"Librarian: {user} borrowing book: {book.title}")
    
    def return_book(self, book, user):
        print(f"Librarian: {user} returning book: {book.title}")
    
    def add_book(self, book):
        print(f"Librarian adding book: {book.title}")
    
    def remove_book(self, book):
        print(f"Librarian removing book: {book.title}")
    
    def generate_borrowings_report(self):
        print(f"Generating borrowings report")
    
    def generate_overdue_books_report(self):
        print(f"Generating overdue books report")
    
    def generate_popularity_report(self):
        print(f"Generating popularity report")

def main():
    book = Book("The Hunger Games", "Suzanne Collins", "Action")
    user = "Kevin Endrijaitis"

    guest = Guest()
    guest.title_search("The Hunger Games")
    guest.author_search("Suzanne Collins")
    guest.genre_search("Action")
    guest.borrow_book(book, user)
    guest.return_book(book, user)

    librarian = Librarian()
    librarian.title_search("The Hunger Games")
    librarian.author_search("Suzanne Collins")
    librarian.genre_search("Action")
    librarian.borrow_book(book, user)
    librarian.return_book(book, user)
    librarian.add_book(book)
    librarian.remove_book(book)
    librarian.generate_borrowings_report()
    librarian.generate_overdue_books_report()
    librarian.generate_popularity_report()

if __name__ == "__main__":
    main()