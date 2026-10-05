import pytest
from library import Book, Library

@pytest.fixture
def sample_library():
    """Fixture to set up a library with sample books for testing."""
    lib = Library()
    lib.add_book(Book("1", "The Hobbit", "J.R.R. Tolkien", "Fantasy"))
    lib.add_book(Book("2", "Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy"))
    lib.add_book(Book("3", "1984", "George Orwell", "Dystopian"))
    lib.add_book(Book("4", "Animal Farm", "George Orwell", "Satire"))
    lib.add_book(Book("5", "Brave New World", "Aldous Huxley", "Dystopian"))
    return lib

def test_search_by_title_exact(sample_library):
    """Test searching for a book with an exact title match."""
    results = sample_library.search_books("1984", search_type="title")
    assert len(results) == 1
    assert results[0].title == "1984"

def test_search_by_title_partial(sample_library):
    """Test searching with a partial title query."""
    results = sample_library.search_books("Ring", search_type="title")
    assert len(results) == 1
    assert results[0].book_id == "2"

def test_search_by_title_case_insensitive(sample_library):
    """Test that search is case-insensitive."""
    results = sample_library.search_books("the hobbit", search_type="title")
    assert len(results) == 1
    assert results[0].book_id == "1"

def test_search_by_author(sample_library):
    """Test retrieving multiple books written by the same author."""
    results = sample_library.search_books("Orwell", search_type="author")
    assert len(results) == 2
    titles = [book.title for book in results]
    assert "1984" in titles
    assert "Animal Farm" in titles

def test_search_by_genre(sample_library):
    """Test searching for books within a specific genre."""
    results = sample_library.search_books("Dystopian", search_type="genre")
    assert len(results) == 2

def test_search_no_results(sample_library):
    """Test search behavior when no matching books exist."""
    results = sample_library.search_books("Nonexistent Book")
    assert len(results) == 0

def test_search_empty_query(sample_library):
    """Test search behavior with an empty query string."""
    results = sample_library.search_books("")
    assert len(results) == 0
