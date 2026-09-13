"""
📚 Topic: Problem2

This script demonstrates problem2 using requests, csv, json and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem2
    2️⃣ how csv.DictWriter fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem2 affects the result.
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
