"""
📚 Topic: Problem3

This script demonstrates problem3 using pydantic dataset validation.

💡 Key points:
1️⃣ the basic syntax for problem3
2️⃣ how validating a list of dicts fits into the example
3️⃣ what to look for when you run the file

🧠 Beginner tip:
Run this file, change one small value, and run it again to see how
problem3 affects the result.
"""

from pydantic import BaseModel, Field, ValidationError


# 3. Given a list of "student score" dicts (some valid, some not),
# split them into clean_records and rejected_records using a
# StudentScore model. A score must be between 0 and 100.
class StudentScore(BaseModel):
    name: str
    score: float = Field(ge=0, le=100)


def process_records(raw_records):
    clean_records = []
    rejected_records = []

    for record in raw_records:
        try:
            clean_records.append(StudentScore(**record))
        except ValidationError:
            rejected_records.append(record)

    return clean_records, rejected_records


raw_data = [
    {"name": "Hamza", "score": 88},
    {"name": "Ali", "score": 105},  # invalid - over 100
    {"name": "Sara", "score": -10},  # invalid - negative
    {"name": "Zoya", "score": 76},
]

clean, rejected = process_records(raw_data)

print(f"✅ {len(clean)} clean records:")
for record in clean:
    print(" -", record)

print(f"\n❌ {len(rejected)} rejected records:")
for record in rejected:
    print(" -", record)
