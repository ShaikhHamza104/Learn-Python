# 📚 Topic: Functional Tools Practice (Exercises)

This folder contains 3 hands-on practice problems designed to reinforce functional programming concepts in Python. The exercises focus on building logging decorators with `*args` and `**kwargs`, creating stateful closures with `nonlocal`, and constructing parameterized decorator factories with `@wraps`.

---

## 📂 What's in this folder

| File | Description |
| --- | --- |
| `problem1.py` | Writing a `@log_call` decorator that logs input arguments, return values, and caught exceptions |
| `problem2.py` | Implementing a closure-based `bank_account()` sharing a private balance between `deposit()` and `withdraw()` |
| `problem3.py` | Authoring a parameterized `@max_calls(limit)` decorator factory enforcing execution call limits |

---

## 💡 Key points

1. **Logging Execution with Decorators (`problem1.py`)**: The `@log_call` wrapper intercepts calls, records both positional `*args` and keyword `**kwargs`, captures the return value, and safely catches exceptions (such as division by zero) without unhandled crashes.
2. **Encapsulating State in Closures (`problem2.py`)**: `bank_account(starting_balance)` returns `(deposit, withdraw)` closures sharing a private `nonlocal balance`, rejecting withdrawals exceeding available funds with clear validation errors.
3. **Decorator Factories & Rate Limiting (`problem3.py`)**: `@max_calls(limit)` constructs a three-level decorator factory maintaining a `nonlocal call_count`, blocking execution with `PermissionError` when the limit is reached, while preserving function metadata via `@wraps(func)`.

---

## 🧠 Beginner tip

Always accept both `*args` and `**kwargs` in your decorator wrappers (`def wrapper(*args, **kwargs):`) and forward both when invoking the wrapped function (`return func(*args, **kwargs)`). Even if your immediate test function only takes positional arguments, omitting `**kwargs` will cause subtle `TypeError` bugs the moment someone calls the decorated function using keyword arguments.

---

## 📊 Where this is used in Data Science

- **API Request Audit Logging**: Telemetry decorators wrap model inference endpoints to log incoming feature payloads, prediction outputs, and execution latency to centralized observability pipelines.
- **Stateful Stateful Preprocessing Pipelines**: Stateful closures maintain running feature statistics (e.g. running min/max or moving averages) during streaming ingestion without global variables.
- **API Rate-Limiting & Quota Management**: In data scraping and batch API querying, decorator factories limit maximum allowed outgoing requests per session or back off when quota limits are reached.

---

## 🏃 How to Run Each Exercise

Execute each problem from the terminal using Python:

```bash
# Problem 1: Log arguments and return values with @log_call
python problem1.py

# Problem 2: Bank account stateful closures
python problem2.py

# Problem 3: Execution call limiter with @max_calls
python problem3.py
```

---

## 📖 Related Lessons

Review the theory of first-class functions, closures, decorators, and `functools` in **[Chapter 19 — Functional Tools](../chapter_19_functional_tools/README.md)**.

---

## ⏭️ What's Next

Learn how to connect to web APIs, parse JSON payloads, and manage external data streams in **[Chapter 20 — APIs & Data Handling](../chapter_20_apis_and_data/README.md)**!
