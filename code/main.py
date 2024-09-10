from pydantic import BaseModel # noqa: D100

class Numbers(BaseModel):
    """A model for holding two integers to be added."""

    a: int
    b: int

def add_numbers(data: Numbers) -> int:
    """Simple function that adds two numbers after validation."""  # noqa: D401
    return data.a + data.b

def substract_numbers(data: Numbers) -> int:
    """Simple function that subtracts two numbers after validation."""  # noqa: D401
    return data.a - data.b

