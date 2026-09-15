"""
📚 Topic: Pydantic Model Validation

This script demonstrates defining Pydantic models with constrained fields
and handling validation outcomes.

💡 Key points:
    1️⃣ Defining models inheriting from `pydantic.BaseModel`
    2️⃣ Applying numerical field boundaries with `Field(ge=..., le=...)`
    3️⃣ Catching and inspecting `pydantic.ValidationError` on invalid data
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
