
## Library Management System
A lightweight, local Library Management System built with Python and tested using pytest. This system allows you to catalog books and search through the collection by title, author, or genre using case-insensitive, partial matching.
## 🚀 Getting Started## Prerequisites
Make sure you have Python 3.10+ and pytest installed.
```
pip install pytest
```
## File Structure
Ensure both files are placed in the same directory:
```
├── library.py             # Main application logic
└── test_book_search.py    # Pytest test suite
```
------------------------------
## 🛠️ Usage Example
You can import the Library and Book classes directly into your own scripts or interactive Python environment:
```
from library import Library, Book
# Initialize the librarylibrary = Library()
# Add books to inventory
library.add_book(Book("1", "The Hobbit", "J.R.R. Tolkien", "Fantasy"))
library.add_book(Book("2", "1984", "George Orwell", "Dystopian"))
# Search by title (partial matching)results = library.search_books("hobbit", search_type="title")
print(f"Found: {results[0].title} by {results[0].author}")
```
------------------------------
## 🧪 Running the Tests
To run the test suite with verbose output, execute the following command in your terminal:
```
pytest test_book_search.py -v
```
## Test Coverage
The suite automatically validates:

* Exact & Partial Matching (e.g., finding "Fellowship of the Ring" by searching "Ring").
* Case Insensitivity (e.g., searching "the hobbit" matches "The Hobbit").
* Multi-Result Queries (e.g., retrieving all books under the "Dystopian" genre or by "George Orwell").
* Edge Cases such as empty search terms or queries returning zero results.
