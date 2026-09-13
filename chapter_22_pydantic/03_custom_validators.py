"""
📚 Topic: Pydantic - Custom Validators

This script demonstrates writing your own validation logic using
@field_validator (for one field) and @model_validator (for rules that
depend on multiple fields at once).

💡 Key points:
1️⃣ the basic syntax for @field_validator
2️⃣ how @model_validator(mode="after") fits into the example
3️⃣ what to look for when you run the file

🧠 Beginner tip:
Run this file, change one small value, and run it again to see how
custom validators affects the result.
"""

from pydantic import BaseModel, field_validator, model_validator
from pydantic import ValidationError


# ---------------------------------------------------
# @field_validator - custom rules for ONE specific field
# ---------------------------------------------------
class SignupForm(BaseModel):
    username: str
    email: str

    @field_validator("username")
    @classmethod
    def username_must_be_lowercase(cls, value):
        if not value.islower():
            raise ValueError("username must be all lowercase")
        return value

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, value):
        if "@" not in value:
            raise ValueError("email must contain an '@' symbol")
        return value


form = SignupForm(username="hamza104", email="hamza@example.com")
print(form)

try:
    bad_form = SignupForm(username="Hamza104", email="not-an-email")
except ValidationError as e:
    print("Validation failed!")
    print(e)


# ---------------------------------------------------
# @model_validator - rules that need MULTIPLE fields together
# ---------------------------------------------------
class DateRange(BaseModel):
    start_date: str
    end_date: str

    @model_validator(mode="after")
    def check_dates_in_order(self):
        # self.start_date and self.end_date are already validated by
        # this point - now we compare them against each other
        if self.start_date > self.end_date:
            raise ValueError("start_date must be before end_date")
        return self


valid_range = DateRange(start_date="2026-01-01", end_date="2026-06-01")
print(valid_range)

try:
    invalid_range = DateRange(start_date="2026-06-01", end_date="2026-01-01")
except ValidationError as e:
    print("Validation failed!")
    print(e)


# ---------------------------------------------------
# 🆚 field_validator vs model_validator
# ---------------------------------------------------
# @field_validator    -> checks ONE field in isolation
# @model_validator     -> checks the WHOLE object after every field
#                         has already passed its own validation


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# Real datasets have business rules that plain types can't express -
# "end date must be after start date", "discount can't exceed price".
# Custom validators let you enforce these rules at the exact moment
# data enters your pipeline, rather than discovering broken rows deep
# inside a groupby() or a trained model's predictions.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Forgetting to `return value` (or `return self`) at the end of a
# validator - Pydantic uses the return value as the field's final
# value, so forgetting it silently replaces your data with None.
