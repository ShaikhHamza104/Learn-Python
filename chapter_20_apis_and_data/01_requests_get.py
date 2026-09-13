"""
📚 Topic: Requests - GET Basics

This script demonstrates how to fetch data from a live API using the
requests library, and how to read the response.

💡 Key points:
    1️⃣ the basic syntax for requests.get()
    2️⃣ how .status_code and .json() fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    requests - get basics affects the result.
"""

# importing requests module : requests is NOT built-in, install it first
# using: pip install requests   (or: uv pip install requests)
import requests

# ---------------------------------------------------
# Making a basic GET request to a free public test API
# ---------------------------------------------------
url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

# status_code tells you if the request worked
# 200 = success, 404 = not found, 500 = server error
print("Status code:", response.status_code)

# .json() converts the response text into a Python dict automatically
data = response.json()
print(data)

# now you can access it just like a normal dictionary
print("Name:", data["name"])
print("Email:", data["email"])
print("City:", data["address"]["city"])


# ---------------------------------------------------
# Getting a LIST of items instead of a single one
# ---------------------------------------------------
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

print(f"\nTotal users fetched: {len(users)}")
for user in users[:3]:  # just showing the first 3
    print(f"- {user['name']} ({user['email']})")


# ---------------------------------------------------
# Sending query parameters (filters) with a request
# ---------------------------------------------------
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}  # only get posts from userId 1

response = requests.get(url, params=params)
posts = response.json()
print(f"\nPosts by userId 1: {len(posts)}")


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# APIs are one of the most common ways real datasets are collected -
# weather data, stock prices, social media stats. Before pandas can
# analyze it, requests is usually what pulls it in.
