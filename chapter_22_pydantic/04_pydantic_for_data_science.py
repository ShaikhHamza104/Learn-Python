"""
📚 Topic: Pydantic for Data Science - Validating Real Datasets

This script ties Pydantic directly to data science work: validating
rows from a CSV before they enter a pandas DataFrame, catching bad
rows instead of silently loading corrupted data.

💡 Key points:
1️⃣ the basic syntax for validating a list of dicts (like CSV rows)
2️⃣ how nested models and TypeAdapter fit into the example
3️⃣ what to look for when you run the file

🧠 Beginner tip:
Run this file, change one small value, and run it again to see how
pydantic for data science affects the result.
"""

from pydantic import BaseModel, Field, ValidationError, TypeAdapter


# ---------------------------------------------------
# Nested models - a model can contain another model as a field
# ---------------------------------------------------
class Address(BaseModel):
    city: str
    country: str


class Customer(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    address: Address  # nested model - validated automatically too


customer = Customer(
    name="Hamza",
    age=21,
    address={"city": "Mumbai", "country": "India"},  # a plain dict works!
)
print(customer)
print(customer.address.city)  # nested access, fully type-checked


# ---------------------------------------------------
# The real data science pattern: validating a whole "dataset" (list
# of dicts) BEFORE it ever touches pandas
# ---------------------------------------------------
class SalesRecord(BaseModel):
    product: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


# imagine this came from a CSV file via csv.DictReader
raw_rows = [
    {"product": "Laptop", "price": 55000, "quantity": 3},
    {"product": "Mouse", "price": 500, "quantity": 10},
    {"product": "Broken Row", "price": -100, "quantity": -5},  # bad data!
    {"product": "Keyboard", "price": "1200", "quantity": "7"},
    # strings, but valid
]

clean_rows = []
rejected_rows = []

for row in raw_rows:
    try:
        record = SalesRecord(**row)
        clean_rows.append(record)
    except ValidationError as e:
        rejected_rows.append((row, e))

print(f"\n✅ {len(clean_rows)} valid rows:")
for record in clean_rows:
    print(" -", record)

print(f"\n❌ {len(rejected_rows)} rejected rows:")
for row, error in rejected_rows:
    print(" -", row, "->", error.error_count(), "error(s)")


# ---------------------------------------------------
# Only clean, validated data goes into pandas
# ---------------------------------------------------
# import pandas as pd
# df = pd.DataFrame([r.model_dump() for r in clean_rows])
# print(df)
#
# (commented out so this file runs without needing pandas installed -
#  uncomment if you have pandas available)


# ---------------------------------------------------
# TypeAdapter - validating a whole list in ONE line, no loop needed
# ---------------------------------------------------
SalesRecordList = TypeAdapter(list[SalesRecord])

only_good_rows = [
    {"product": "Laptop", "price": 55000, "quantity": 3},
    {"product": "Mouse", "price": 500, "quantity": 10},
]

validated_list = SalesRecordList.validate_python(only_good_rows)
print(f"\nValidated {len(validated_list)} records in one call")


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# This "validate then reject" pattern is exactly what production data
# pipelines do: read raw rows, run them through a Pydantic model, keep
# the clean ones, log/quarantine the bad ones. It replaces a pile of
# manual if-checks with a single, reusable, self-documenting schema -
# and it's the same validation approach used by FastAPI, LangChain,
# and most modern Python data tooling.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Validating data AFTER loading it into a pandas DataFrame instead of
# BEFORE. By then, pandas may have already silently converted a bad
# value to NaN or the wrong dtype - validate at the door, not after.
