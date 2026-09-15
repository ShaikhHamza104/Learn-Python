# 📚 Topic: APIs & Data Handling

Modern software relies heavily on external data sources. Application Programming Interfaces (APIs) allow programs to communicate over HTTP to fetch datasets, post metrics, and query live cloud services. This chapter covers the third-party `requests` library, issuing HTTP `GET` requests, parsing JSON responses into native Python dictionaries, resilient error handling with timeouts and `raise_for_status()`, and persisting downloaded payloads to disk using `json` and `pathlib`.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_requests_get.py` | Basic HTTP `GET` requests, inspecting `.status_code`, parsing with `.json()`, and query parameters (`params`) |
| `02_requests_error_handling.py` | Robust API error handling with `raise_for_status()`, timeouts, specific exception types, and logging |
| `03_save_api_response_to_json.py` | End-to-end data acquisition: querying an API, formatting with `json.dumps()`, and saving via `pathlib` |

---

## 💡 Key points

1. **HTTP GET Requests (`01_requests_get.py`)**: `requests.get(url)` connects to a remote REST endpoint. Inspecting `response.status_code` checks HTTP response health (e.g. `200` OK, `404` Not Found, `500` Server Error).
2. **Automatic JSON Deserialization (`01_requests_get.py`)**: Calling `response.json()` automatically parses JSON payloads into native Python dictionaries or lists, eliminating manual parsing.
3. **Query Parameters (`01_requests_get.py`)**: Passing a dictionary into `requests.get(url, params={"userId": 1})` cleanly constructs parameterized query strings (`?userId=1`) without manual string formatting.
4. **Enforcing Response Statuses (`02_requests_error_handling.py`)**: By default, `requests.get()` does not raise an exception on HTTP `4xx` or `5xx` statuses. Invoking `response.raise_for_status()` turns client and server error codes into catchable `requests.exceptions.HTTPError` exceptions.
5. **Defensive Network Timeouts (`02_requests_error_handling.py`)**: Always set a timeout (e.g. `timeout=5`) to prevent requests from hanging indefinitely on stalled network connections. Handle failures using specific exceptions: `Timeout`, `ConnectionError`, `HTTPError`, and the base `RequestException`.
6. **Data Ingestion & Persistence (`03_save_api_response_to_json.py`)**: Complete data pipelines combine `requests` for fetching, `Path("api_output").mkdir(exist_ok=True)` for directory safety, and `Path.write_text(json.dumps(data, indent=4))` for persistent disk storage.

---

## 🧠 Beginner tip

Never make a production API call without specifying a `timeout` argument (e.g., `requests.get(url, timeout=10)`). Without an explicit timeout, Python will wait indefinitely if the remote server drops the connection without responding, hanging your script or pipeline forever. Additionally, always chain `response.raise_for_status()` before calling `response.json()` to avoid cryptic JSON decoding errors when an endpoint returns an HTML error page.

---

## 📊 Where this is used in Data Science

- **Live Market & Telemetry Ingestion**: Automated trading and time-series pipelines fetch intraday stock prices, crypto order books, and IoT sensor streams from REST APIs on a scheduled cron cadence.
- **Enriching Machine Learning Datasets**: ETL pipelines call external geospatial and demographic APIs (e.g., Google Maps API, OpenWeatherMap) to append weather and coordinates to raw customer tabular records.
- **Model Deployment & Inference Testing**: ML engineers interact with deployed FastAPI/Flask inference servers, sending feature payloads and validating JSON prediction scores.

---

## 🛠️ Code Examples

### Querying an API with Filtering Parameters
```python
import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}

response = requests.get(url, params=params, timeout=5)
response.raise_for_status()

comments = response.json()
print(f"Retrieved {len(comments)} comments for post 1")
```

### Resilient Request Wrapper
```python
import logging
import requests

def safe_api_get(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        logging.error("Request timed out.")
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        logging.error(f"Network error: {err}")
    return None
```

### Persisting API Payloads to Disk with `pathlib`
```python
import json
from pathlib import Path

def save_payload(data, destination_path):
    dest = Path(destination_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, indent=2))
    print(f"Saved payload to {dest.resolve()}")
```

---

## 🏋️ Practice Exercises

Build API scrapers, robust error handlers, and file persistence pipelines in **[chapter_20_apis_and_data_exercises/](../chapter_20_apis_and_data_exercises/README.md)**!

---

## ⏭️ What's Next

Bring together everything you have learned across all 20 chapters to build comprehensive real-world applications in **[Chapter 21 — Capstone Projects](../chapter_21_capstone/README.md)**!
