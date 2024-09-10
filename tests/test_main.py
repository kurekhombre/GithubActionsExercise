import pytest  # noqa: D100
from pydantic import ValidationError
from code.main import add_numbers, Numbers

def test_add_numbers():
    """Test that the add_numbers function correctly adds two integers."""
    numbers = Numbers(a=2, b=3)
    assert add_numbers(numbers) == 5

def test_add_numbers_invalid_type():
    """Test that the Numbers model raises a ValidationError when a non-integer is passed."""  # noqa: E501
    with pytest.raises(ValidationError):
        Numbers(a=2, b="three")
