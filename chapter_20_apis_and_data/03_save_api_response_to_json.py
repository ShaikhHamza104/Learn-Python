"""
📚 Topic: Save API Response to JSON

This script demonstrates fetching data from an API and saving it to
disk, tying together requests, json, and pathlib from earlier chapters.

💡 Key points:
    1️⃣ the basic syntax for combining requests with json.dump
    2️⃣ how pathlib fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    save api response to json affects the result.
"""

import json
import logging
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------------------------------------
# Step 1 : make sure an "output" folder exists to save data into
# ---------------------------------------------------
output_folder = Path("api_output")
output_folder.mkdir(exist_ok=True)


# ---------------------------------------------------
# Step 2 : fetch data from the API, with proper error handling
# ---------------------------------------------------
def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch data: {e}")
        return None


# ---------------------------------------------------
# Step 3 : save the fetched data as a JSON file using pathlib
# ---------------------------------------------------
def save_to_json(data, filename):
    if data is None:
        logging.warning("No data to save - skipping")
        return

    file_path = output_folder / filename
    file_path.write_text(json.dumps(data, indent=4))
    logging.info(f"Saved data to {file_path}")


# ---------------------------------------------------
# Putting it all together
# ---------------------------------------------------
url = "https://jsonplaceholder.typicode.com/users"
users = fetch_data(url)
save_to_json(users, "users.json")

# reading it back, to prove it actually saved correctly
saved_file = output_folder / "users.json"
if saved_file.exists():
    loaded_data = json.loads(saved_file.read_text())
    print(f"Loaded {len(loaded_data)} users back from users.json")
    print("First user:", loaded_data[0]["name"])


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# This exact pattern - fetch, error-handle, save to disk - is the
# foundation of almost every simple data collection script you'll
# write before a project graduates to a full pandas/database pipeline.
