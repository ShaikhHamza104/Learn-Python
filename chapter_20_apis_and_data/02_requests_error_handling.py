"""
📚 Topic: Requests - Error Handling

This script demonstrates how to handle common API failures - timeouts,
connection errors, and bad status codes - using try/except and logging.

💡 Key points:
    1️⃣ the basic syntax for raise_for_status()
    2️⃣ how try/except and logging fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    requests - error handling affects the result.
"""

import logging
import requests

logging.basicConfig(
    filename="api_errors.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ---------------------------------------------------
# The problem: a plain requests.get() does NOT crash on a 404 or 500
# ---------------------------------------------------
url = "https://jsonplaceholder.typicode.com/users/9999"  # doesn't exist
response = requests.get(url)
print("Status code:", response.status_code)  # 404, but no error raised!


# ---------------------------------------------------
# raise_for_status() : turns a bad status code into a real exception
# ---------------------------------------------------
def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raises an error for 4xx/5xx codes
        logging.info(f"Successfully fetched user {user_id}")
        return response.json()

    except requests.exceptions.HTTPError:
        logging.error(f"User {user_id} not found (bad status code)")
        return None

    except requests.exceptions.ConnectionError:
        logging.error("Could not connect - check your internet connection")
        return None

    except requests.exceptions.Timeout:
        logging.error("The request took too long and timed out")
        return None

    except requests.exceptions.RequestException as e:
        # catches ANY other requests-related error we didn't expect
        logging.exception(f"Unexpected error while fetching user: {e}")
        return None


# a real, existing user - should succeed
user = fetch_user(1)
if user:
    print("Found user:", user["name"])

# a fake user id - should be handled gracefully, not crash the program
user = fetch_user(9999)
if user is None:
    print("Could not fetch that user - check api_errors.log for details")


# ---------------------------------------------------
# 🆚 Without error handling vs with error handling
# ---------------------------------------------------
# Without: response = requests.get(url)   -> silently returns a 404
# With:    response.raise_for_status()    -> raises HTTPError you can
#                                             catch and log properly


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# A data pipeline that pulls from an API daily WILL eventually hit a
# timeout or a dead endpoint. Catching and logging these errors means
# your pipeline can skip the bad request and keep going, instead of
# crashing the whole job.
