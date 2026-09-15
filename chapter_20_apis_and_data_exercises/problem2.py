"""
📚 Topic: Exporting API Responses to JSON and CSV

This script fetches data from a remote REST API and persists the records to
both JSON and CSV files.

💡 Key points:
    1️⃣ Deserializing API responses with `response.json()`
    2️⃣ Writing formatted JSON files with `json.dump(..., indent=4)`
    3️⃣ Writing tabular data to CSV with `csv.DictWriter`
"""


import csv
import json

import requests


# 2. Write a program that fetches all posts from the API and saves
# them as BOTH a JSON file and a CSV file.
def save_posts_as_json_and_csv():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        posts = response.json()

        # save as JSON
        with open("posts.json", "w") as file:
            json.dump(posts, file, indent=4)
        print("Saved posts.json")

        # save as CSV
        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=posts[0].keys())
            writer.writeheader()
            writer.writerows(posts)
        print("Saved posts.csv")

    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")
    except (IndexError, KeyError) as e:
        print(f"Unexpected data format from API: {e}")


save_posts_as_json_and_csv()
