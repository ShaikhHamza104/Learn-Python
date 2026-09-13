"""
📚 Topic: Pydantic - Field Constraints

This script demonstrates using Field() to add extra validation rules
beyond a plain type hint - minimums, maximums, defaults, and metadata.

💡 Key points:
1️⃣ the basic syntax for Field() constraints (gt, ge, lt, le, min_length)
2️⃣ how Annotated fits into the example
3️⃣ what to look for when you run the file

🧠 Beginner tip:
Run this file, change one small value, and run it again to see how
field constraints affects the result.
"""

from pydantic import BaseModel, Field, ValidationError
from typing import Annotated


# ---------------------------------------------------
# Field() lets you add rules on top of a normal type hint
# ---------------------------------------------------
class Product(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0)  # gt = "greater than"
    quantity: int = Field(ge=0, default=0)  # ge = "greater than or equal"
    rating: float = Field(ge=0, le=5)  # between 0 and 5 inclusive


product = Product(name="Keyboard", price=29.99, quantity=10, rating=4.5)
print(product)


# ---------------------------------------------------
# Violating a constraint raises a ValidationError, just like a bad type
# ---------------------------------------------------
try:
    bad_product = Product(name="", price=-5, rating=10)
except ValidationError as e:
    print("Validation failed!")
    print(e)


# ---------------------------------------------------
# Field() can also add documentation and aliases
# ---------------------------------------------------
class Student(BaseModel):
    full_name: str = Field(alias="fullName")  # accept camelCase input
    score: float = Field(ge=0, le=100, description="Score out of 100")


# incoming data (like from a JSON API) often uses camelCase
incoming_data = {"fullName": "Zoya", "score": 92.5}
student = Student(**incoming_data)
print(student)
print(student.full_name)  # accessed with the Python-style name


# ---------------------------------------------------
# Annotated[] - the modern way to attach a Field to a type hint
# ---------------------------------------------------

Age = Annotated[int, Field(ge=0, le=120)]


class Person(BaseModel):
    name: str
    age: Age


person = Person(name="Hamza", age=21)
print(person)


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# Field constraints are how you encode real-world data rules directly
# into your validation layer - a rating really CAN'T be 10 out of 5,
# a price really CAN'T be negative. Catching these at the door means
# your analysis never has to defensively check for impossible values.
