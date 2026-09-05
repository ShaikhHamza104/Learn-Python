"""
📚 Topic: 12 Exception Logging

This script demonstrates 12 exception logging using for loops, conditions,
functions and exception handling.

💡 Key points:
    1️⃣ the basic syntax for 12 exception logging
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    12 exception logging affects the result.
"""


# 🧯 Combining Exception Handling + Logging
# This is the pattern used in almost every real-world Python project:
# when something goes wrong, don't just print it - LOG it properly.

import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# ---------------------------------------------------
# ❌ 1. The "beginner" way (what we did back in chapter_12 basics)
# ---------------------------------------------------
def divide_beginner_way(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: cannot divide by zero")


# ---------------------------------------------------
# ✅ 2. The "real project" way - log it instead of just printing
# ---------------------------------------------------
def divide_proper_way(a, b):
    try:
        result = a / b
        logging.info(f"Divided {a} by {b}, got {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Tried to divide {a} by zero!")
        return None


divide_proper_way(10, 0)


# ---------------------------------------------------
# 🔍 3. logging.exception() - the BEST way inside an except block
# ---------------------------------------------------
# logging.exception() automatically includes the full error traceback
# in your log file - super useful for debugging later
def divide_with_traceback(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.exception("Division failed - full details below:")
        return None


divide_with_traceback(5, 0)
# check errors.log after running this - you'll see the FULL traceback saved,
# not just "cannot divide by zero"


# ---------------------------------------------------
# 🧑‍💻 4. A more real example - reading a file that might not exist
# ---------------------------------------------------
def read_config_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"Config file '{filename}' was not found")
        return None
    except PermissionError:
        logging.error(f"No permission to read '{filename}'")
        return None
    else:
        logging.info(f"Successfully read '{filename}'")
    finally:
        logging.info("Finished attempting to read config file")


read_config_file("config.txt")


# ---------------------------------------------------
# 🧠 Quick recap - where does each log level go in a try/except?
# ---------------------------------------------------
# try block succeeded        -> logging.info()
# something minor is off     -> logging.warning()
# an exception was caught    -> logging.error() or logging.exception()
# the whole program is dying -> logging.critical()


# ---------------------------------------------------
# 💡 Why does this matter for Data Science?
# ---------------------------------------------------
# Imagine a script that processes 10,000 rows of a dataset and row #4,532
# has bad data and crashes it. Without logging, you have no idea which row
# caused the problem. With logging.exception() inside your except block,
# your log file tells you exactly which row and exactly why.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Using logging.error() when you actually want logging.exception().
# error() just logs your message - exception() logs your message PLUS
# the full traceback. Always use exception() inside an except block.
