class Book:
    def __init__(self, book_id: str, title: str, author: str, genre: str, available: bool = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        """Adds a book to the library inventory."""
        self.books[book.book_id] = book

    def search_books(self, query: str, search_type: str = "title") -> list[Book]:
        """
        Searches for books by title, author, or genre.
        The search is case-insensitive and matches partial strings.
        """
        if not query:
            return []
            
        query = query.lower()
        results = []
        
        for book in self.books.values():
            if search_type == "title" and query in book.title.lower():
                results.append(book)
            elif search_type == "author" and query in book.author.lower():
                results.append(book)
            elif search_type == "genre" and query in book.genre.lower():
                results.append(book)
                
        return results

