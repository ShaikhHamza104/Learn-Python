# 📚 Topic: APIs & Data Handling Practice (Exercises)

This folder contains 2 practical exercises applying API interaction techniques learned in Chapter 20. The problems cover querying REST endpoints with query filters, extracting and filtering nested JSON datasets, and exporting multi-record payloads to both JSON and structured CSV file formats.

---

## 📂 What's in this folder

| File | Description |
| --- | --- |
| `problem1.py` | Querying user todo lists via API parameters and filtering pending (incomplete) items |
| `problem2.py` | Fetching API post records and saving dual export formats: `posts.json` and `posts.csv` with `csv.DictWriter` |

---

## 💡 Key points

1. **Filtering API Results with Parameters (`problem1.py`)**: Demonstrates requesting filtered endpoint data using `params={"userId": user_id}`, validating success via `response.raise_for_status()`, and using a list comprehension to isolate uncompleted tasks (`not todo["completed"]`).
2. **Dual JSON and CSV Data Serialization (`problem2.py`)**: Fetches remote records, dumps formatted JSON using `json.dump(posts, file, indent=4)`, and transforms the list of dictionaries into a tabular CSV file using `csv.DictWriter(file, fieldnames=posts[0].keys())`.

---

## 🧠 Beginner tip

When writing dictionary records to a CSV file using `csv.DictWriter`, always pass `newline=""` into `open("output.csv", "w", newline="")`. On Windows systems, omitting `newline=""` will cause Python to insert extra blank rows between data lines because Windows line endings (`\r\n`) get double-translated by default file stream writers.

---

## 📊 Where this is used in Data Science

- **Automated Data Lake Extract-Load (EL)**: Ingestion workers pull records from third-party enterprise APIs and serialize raw payloads into compressed JSON dumps alongside flattened tabular CSV or Parquet files for analytical querying.
- **Task & Workflow Monitoring**: Automated DevOps or data quality alerts query project management APIs (Jira, GitHub Issues) to identify unclosed or stale workflow tickets and dispatch notifications.
- **Format Conversion for BI Dashboards**: Extracting API payloads and saving clean CSV exports allows downstream analysts without Python programming skills to import fresh datasets directly into Excel, Tableau, or Power BI.

---

## 🏃 How to Run Each Exercise

Execute each problem from the terminal using Python:

```bash
# Problem 1: Query and filter pending user todos
python problem1.py

# Problem 2: Fetch posts and export to posts.json and posts.csv
python problem2.py
```

---

## 📖 Related Lessons

Review the complete foundations of HTTP requests, status handling, and serialization in **[Chapter 20 — APIs & Data Handling](../chapter_20_apis_and_data/README.md)**.

---

## ⏭️ What's Next

Synthesize all your skills across Python basics, OOP, error handling, filesystem manipulation, iterators, and APIs in **[Chapter 21 — Capstone Projects](../chapter_21_capstone/README.md)**!
