"""
📚 Topic: Pydantic Custom Field Validators

This script demonstrates custom field validation logic using Pydantic's
`@field_validator` decorator.

💡 Key points:
    1️⃣ Implementing custom validation methods with `@field_validator`
    2️⃣ Validating complex constraints (minimum length and digit presence)
    3️⃣ Raising informative `ValueError` exceptions upon validation failure
"""


from pydantic import BaseModel, field_validator, ValidationError


# 2. Build a Password model with a custom validator that rejects any
# password shorter than 8 characters or missing a digit.
class Password(BaseModel):
    value: str

    @field_validator("value")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("password must be at least 8 characters")
        if not any(char.isdigit() for char in value):
            raise ValueError("password must contain at least one digit")
        return value


def check_password(raw_password):
    try:
        Password(value=raw_password)
        print(f"'{raw_password}' is a strong password ✅")
    except ValidationError as e:
        print(f"'{raw_password}' is weak ❌")
        print(e)


check_password("hamza2026")
check_password("short1")
check_password("nodigitshere")
