"""
📚 Topic: Dataset Validation & Record Splitting

This script processes a batch of raw records, partitioning them into clean
and rejected datasets using a Pydantic model.

💡 Key points:
    1️⃣ Iterating through raw heterogeneous record collections
    2️⃣ Validating individual items against schema definitions
    3️⃣ Segregating valid model instances from rejected records with errors
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
