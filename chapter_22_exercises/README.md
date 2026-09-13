# 📚 Topic: Pydantic Practice (Exercises)

This folder contains 3 practical exercises testing your ability to define Pydantic schemas, enforce numeric and string constraints, write custom field validators, and sanitize batch datasets in data engineering workflows.

---

## 📂 What's in this folder

| File | Description |
| --- | --- |
| `problem1.py` | Building a `MovieReview` schema with bounded rating constraints (`0 <= rating <= 10`) and handling valid vs. invalid review payloads |
| `problem2.py` | Creating a `Password` model equipped with a custom `@field_validator` enforcing length and digit requirements |
| `problem3 .py` | Building a defensive data-cleaning pipeline that processes a list of raw student score records, segregating clean models from rejected rows |

---

## 💡 Key points

1. **Schema Validation (`problem1.py`)**: Uses `Field(ge=0, le=10)` to enforce that movie ratings cannot fall outside the 0–10 scale, catching out-of-bound errors via `try...except ValidationError`.
2. **Custom Field Validators (`problem2.py`)**: Uses `@field_validator("value")` with `@classmethod` to ensure password strings are at least 8 characters long and contain at least one numerical digit.
3. **Dataset Ingestion & Segregation (`problem3 .py`)**: Iterates through untrusted dictionary records, instantiates `StudentScore(**record)`, and neatly partitions incoming rows into `clean_records` and `rejected_records`.

---

## 🧠 Beginner tip

When validating datasets iteratively with Pydantic models, always catch `ValidationError` specifically inside your processing loop. Never use a bare `except:` clause, as that can mask critical syntax errors or keyboard interrupts (`Ctrl+C`).

---

## 📊 Where this is used in Data Science

- **ETL Data Cleaning**: Real-world data ingestion pipelines encounter incomplete, out-of-bounds, or misformatted rows. Partitioning valid records from invalid ones ensures downstream analytics and ML training sets are free of garbage data.
- **Form & Auth Validation**: User signups, password policies, and content submissions require robust client/server validation before saving into SQL or NoSQL databases.

---

## 🏃 How to Run Each Exercise

Execute each problem directly from the terminal:

```bash
# Problem 1: Movie review validation
python chapter_22_exercises/problem1.py

# Problem 2: Password validator
python chapter_22_exercises/problem2.py

# Problem 3: Student score dataset cleaner
python "chapter_22_exercises/problem3 .py"
```

---

## 📖 Related Lessons

Review the core concepts of Pydantic models, field constraints, and custom validators in **[Chapter 22 — Pydantic](../chapter_22_pydantic/README.md)**.
