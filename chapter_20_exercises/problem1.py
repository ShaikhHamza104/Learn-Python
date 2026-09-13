"""
📚 Topic: Problem1

This script demonstrates problem1 using requests, functions and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem1
    2️⃣ how requests fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem1 affects the result.
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
