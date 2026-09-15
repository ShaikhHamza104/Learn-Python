"""
📚 Topic: Fetching Filtered API Data

This script demonstrates fetching data from a REST API with query parameters
and filtering responses.

💡 Key points:
    1️⃣ Using `requests.get()` with query parameter dictionaries
    2️⃣ Checking HTTP status codes with `response.raise_for_status()`
    3️⃣ Filtering parsed JSON records conditionally
"""


import requests


# 1. Write a program that fetches all "to-do" items for a given user
# from the API and prints only the ones that are NOT completed yet.
def get_pending_todos(user_id):
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        todos = response.json()

        pending = [todo for todo in todos if not todo["completed"]]

        print(f"User {user_id} has {len(pending)} pending todos:")
        for todo in pending:
            print(f"- {todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")


get_pending_todos(1)
