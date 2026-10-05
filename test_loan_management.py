import pytest
from library import Library, Book

@pytest.fixture
def library_with_resources():
    """Provides a setup library with one book and two registered members."""
    lib = Library()
    lib.add_book(Book("B100", "Design Patterns", "Gang of Four", "Tech"))
    lib.register_member("M200", "John Doe", "john@example.com")
    lib.register_member("M300", "Jane Doe", "jane@example.com")
    return lib

def test_issue_loan_success(library_with_resources):
    """Verifies that a registered member can successfully borrow an available book."""
    lib = library_with_resources
    
    result = lib.issue_loan(member_id="M200", book_id="B100")
    
    assert result is True
    assert lib.books["B100"].available is False
    assert lib.loans["B100"] == "M200"

def test_issue_loan_book_already_borrowed(library_with_resources):
    """Verifies that a book cannot be loaned out if its availability is False."""
    lib = library_with_resources
    lib.issue_loan(member_id="M200", book_id="B100")
    
    with pytest.raises(ValueError, match="Book is not available"):
        lib.issue_loan(member_id="M300", book_id="B100")

@pytest.mark.parametrize("m_id, b_id", [
    ("INVALID_MEMBER", "B100"),
    ("M200", "INVALID_BOOK"),
    ("INVALID_MEMBER", "INVALID_BOOK")
])
def test_issue_loan_invalid_ids_raise_error(library_with_resources, m_id, b_id):
    """Verifies errors are raised if the book or member doesn't exist in the system."""
    lib = library_with_resources
    
    with pytest.raises(ValueError, match="Member or Book not found"):
        lib.issue_loan(member_id=m_id, book_id=b_id)

def test_return_loan_success(library_with_resources):
    """Verifies returning a checked-out book clears records and resets availability."""
    lib = library_with_resources
    lib.issue_loan(member_id="M200", book_id="B100")
    
    result = lib.return_loan(book_id="B100")
    
    assert result is True
    assert lib.books["B100"].available is True
    assert "B100" not in lib.loans

def test_return_loan_not_borrowed_raises_error(library_with_resources):
    """Verifies that returning an unborrowed book throws an explicit error."""
    lib = library_with_resources
    
    with pytest.raises(ValueError, match="Book was not checked out"):
        lib.return_loan(book_id="B100")

def test_return_loan_invalid_book_raises_error(library_with_resources):
    """Verifies that trying to return a non-existent book ID raises a Book not found error."""
    lib = library_with_resources
    
    with pytest.raises(ValueError, match="Book not found"):
        lib.return_loan(book_id="NON_EXISTENT")
