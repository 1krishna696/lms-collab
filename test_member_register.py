import pytest
from library import Library

@pytest.fixture
def empty_library():
    """Provides a fresh Library instance for every test."""
    return Library()

def test_register_member_success(empty_library):
    """Verifies that a valid member can be successfully registered."""
    member = empty_library.register_member("M001", "Alice Smith", "alice@example.com")
    
    assert "M001" in empty_library.members
    assert empty_library.members["M001"].name == "Alice Smith"
    assert member.email == "alice@example.com"

def test_register_member_duplicate_id(empty_library):
    """Verifies that registering a member with an existing ID raises an error."""
    empty_library.register_member("M001", "Alice Smith", "alice@example.com")
    
    with pytest.raises(ValueError, match="already registered"):
        empty_library.register_member("M001", "Bob Jones", "bob@example.com")

@pytest.mark.parametrize("m_id, name, email", [
    ("", "Alice", "alice@example.com"),
    ("M001", "", "alice@example.com"),
    ("M001", "Alice", ""),
    ("", "", "")
])
def test_register_member_empty_fields(empty_library, m_id, name, email):
    """Verifies that missing information raises a validation error."""
    with pytest.raises(ValueError, match="required"):
        empty_library.register_member(m_id, name, email)
