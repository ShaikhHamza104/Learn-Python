# 📚 Topic: Capstone Project - Currency Exchange Rate Toolkit

A CLI application that fetches, validates, stores, and analyzes
currency exchange-rate data - tying together API integration, data
validation, persistence, and Pandas analysis into one working
pipeline, instead of 20 separate isolated exercises.

Data comes from the free [Frankfurter API](https://www.frankfurter.dev)
(no API key required).

---

## 📂 What's in this folder

| File | Role |
| --- | --- |
| `fetcher.py` | Calls the Frankfurter API and handles network failures (timeouts, connection errors, bad status codes) |
| `validator.py` | Validates raw API responses against a Pydantic schema before anything is trusted |
| `storage.py` | Persists validated records to DuckDB and loads them back, including straight into a Pandas DataFrame |
| `analyzer.py` | Computes summary stats, day-over-day change, and rolling averages using Pandas |
| `main.py` | The CLI entry point - wires the four pieces above together behind a menu |

---

## 🏗️ Architecture

```
User input
    │
    ▼
main.py (CapstoneApp)
    │
    ├─► fetcher.py      ExchangeRateFetcher   → raw dict/list from the API
    │                    (raises FetchError on network/API failure)
    │
    ├─► validator.py    validate_single / validate_records
    │                    (raises ValidationError on bad data shape)
    │
    ├─► storage.py       ExchangeRateRepository  → DuckDB (capstone.duckdb)
    │
    └─► analyzer.py      ExchangeRateAnalyzer    → summary / trends via Pandas
```

Each stage only trusts what the stage before it has already checked:
`fetcher.py` doesn't validate data shape, `validator.py` doesn't know
about the network, and `storage.py` never re-validates what it reads
back out - because it was already validated once, on the way in.

---

## ▶️ How to run

```bash
pip install requests pydantic duckdb pandas
python main.py
```

Then use the menu to fetch a rate, fetch a date range, view what's
stored, or analyze it. All data persists in `capstone.duckdb` between
runs.

---

## 💡 Key design decisions

1. **`__init__` only sets up state - `run()` starts the app.**
   `CapstoneApp()` doesn't immediately prompt for input the moment
   it's created; you have to call `.run()` explicitly. This is the
   direct opposite of an earlier mistake in `projects/Library
   Management System`, where creating the object started an
   interactive loop inside `__init__` - making it untestable.

2. **Custom exceptions collapse many failure types into one.**
   `requests` can fail five different ways (timeout, connection
   error, bad status, etc.) - `fetcher.py` catches all of them and
   re-raises a single `FetchError`, so `main.py` only ever needs one
   `except FetchError` block, not five.

3. **Input is validated locally before it ever reaches the API.**
   Empty currency codes, malformed dates (`2026-15-9`), and
   same-currency conversions (`USD` → `USD`) are all caught in
   `main.py` before a network request is made - so users get an
   immediate, specific message instead of a raw HTTP error.

4. **Validation happens once, at the boundary.**
   Every record from the API passes through a Pydantic model in
   `validator.py` before it's allowed into storage. Bad rows are
   logged and skipped individually - one corrupted row never crashes
   a whole batch fetch.

5. **Storage hands back data shaped for its next use.**
   `load_all()` returns plain dicts for display; `load_as_dataframe()`
   returns a Pandas DataFrame, using DuckDB's native `.df()` method -
   no manual loop rebuilding rows into a DataFrame is needed.

---

## 📊 Where this is used in Data Science

This mirrors a real (miniature) data pipeline: ingest → validate →
persist → analyze. Production data science and data engineering work
looks like this at a larger scale - scheduled jobs pulling from APIs,
schema validation before data touches a warehouse, and analysis
layered on top of trusted, stored data.

---

## ✅ Status

All 5 milestones complete and manually tested, including the
edge cases below (found by actually using the app, not by guessing):

- Empty currency input
- Invalid/malformed dates (e.g. `2026-15-9`)
- Currency codes that look valid but aren't recognized by the API
  (e.g. `USA`)
- Requesting a currency the same as the base currency (`USD` → `USD`)