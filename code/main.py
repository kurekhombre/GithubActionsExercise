from pydantic import BaseModel, ValidationError  # noqa: D100

class Numbers(BaseModel):
    """A model for holding two integers to be added."""

    a: int
    b: int

def add_numbers(data: Numbers) -> int:
    """Simple function that adds two numbers after validation."""  # noqa: D401
    return data.a + data.b

if __name__ == "__main__":
    try:
        # Example with incorrect type for `b`, this will raise a validation error
        numbers = Numbers(a=2, b="3")
        result = add_numbers(numbers)
        print(f"Result: {result}")
    except ValidationError as e:
        print(f"Validation error: {e}")
