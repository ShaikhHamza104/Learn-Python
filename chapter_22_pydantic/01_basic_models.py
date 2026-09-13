"""
📚 Topic: Pydantic - Basic Models & Validation

This script demonstrates the core idea behind Pydantic: defining the
shape of your data with normal Python type hints, and letting
Pydantic automatically validate and convert incoming data to match.

💡 Key points:
1️⃣ the basic syntax for defining a BaseModel
2️⃣ how automatic type coercion and ValidationError fit into the example
3️⃣ what to look for when you run the file

🧠 Beginner tip:
Run this file, change one small value, and run it again to see how
pydantic basics affects the result.
"""

# pydantic is NOT built-in, install it first:
# pip install pydantic   (or: uv pip install pydantic)
from pydantic import BaseModel, ValidationError


# ---------------------------------------------------
# A Pydantic model is just a class with type-annotated fields
# ---------------------------------------------------
class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True  # default value - this field is optional


# ---------------------------------------------------
# Creating an instance validates the data automatically
# ---------------------------------------------------
user = User(id=1, name="Hamza", age=21)
print(user)
print(user.name, user.age)


# ---------------------------------------------------
# Pydantic tries to COERCE compatible types, not just reject them
# ---------------------------------------------------
# Notice: id and age are passed as STRINGS here, but the model says int
user2 = User(id="2", name="Ali", age="25")
print(user2)
print(type(user2.id), type(user2.age))  # both become real ints


# ---------------------------------------------------
# When data genuinely doesn't fit, Pydantic raises a ValidationError
# ---------------------------------------------------
try:
    bad_user = User(id="not-a-number", name="Sara", age=20)
except ValidationError as e:
    print("Validation failed!")
    print(e)


# ---------------------------------------------------
# Converting a model back to plain Python / JSON
# ---------------------------------------------------
print(user.model_dump())  # -> a plain dict
print(user.model_dump_json())  # -> a JSON string


# ---------------------------------------------------
# 🆚 Pydantic vs a plain dict
# ---------------------------------------------------
# plain dict:  no guarantee "age" is really an int - could be anything
# Pydantic:    "age" is GUARANTEED to be an int by the time you use it,
#              or you get a clear error immediately, not a bug later


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# Every dataset you load from a CSV, JSON API, or user form is really
# just "a pile of dicts with no guaranteed types". Pydantic lets you
# define what a valid row SHOULD look like, and catches bad rows
# immediately instead of letting them silently corrupt a pandas
# DataFrame or crash a model deep inside a pipeline.
