"""
📚 Topic: Problem1

This script demonstrates problem1 using pydantic models and
validation.

💡 Key points:
1️⃣ the basic syntax for problem1
2️⃣ how BaseModel fit into the example
3️⃣ what to look for when you run the file

🧠 Beginner tip:
Run this file, change one small value, and run it again to see how
problem1 affects the result.
"""

from pydantic import BaseModel, Field, ValidationError


# 1. Build a MovieReview model: title (str), rating (float, 0-10),
# reviewer (str). Try creating one valid and one invalid review.
class MovieReview(BaseModel):
    title: str
    rating: float = Field(ge=0, le=10)
    reviewer: str


def create_review(data):
    try:
        review = MovieReview(**data)
        print("Valid review:", review)
    except ValidationError as e:
        print("Invalid review:")
        print(e)


create_review({"title": "Interstellar", "rating": 9.5, "reviewer": "Hamza"})
create_review({"title": "Bad Movie", "rating": 15, "reviewer": "Ali"})
