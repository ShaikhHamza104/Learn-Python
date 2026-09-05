"""
📚 Topic: 11 Logging Basics

This script demonstrates 11 logging basics using for loops, functions and
imports.

💡 Key points:
    1️⃣ the basic syntax for 11 logging basics
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    11 logging basics affects the result.
"""


# 📝 Introduction to Logging
# So far we've been using print() to debug our code.
# print() is fine for tiny scripts, but real projects use "logging" instead.
# Logging lets you save messages to a FILE, add timestamps, and control
# how serious each message is - print() can't do any of that.

import logging

# ---------------------------------------------------
# ⚙️ 1. Basic setup (do this once at the top of your script)
# ---------------------------------------------------
logging.basicConfig(
    level=logging.INFO,  # show INFO messages and above
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# now instead of print("something happened"), we do:
logging.info("Program started")


# ---------------------------------------------------
# 🎚️ 2. The 5 logging levels (from least to most serious)
# ---------------------------------------------------
logging.debug("This is a debug message")  # detailed info, for developers
logging.info("This is an info message")  # general "this happened" message
logging.warning("This is a warning message")  # something looks off
logging.error("This is an error message")  # something failed
logging.critical("This is a critical message")  # program might crash

# NOTE: debug() won't show up above because we set level=logging.INFO
# INFO level means: show INFO and anything MORE serious than INFO
# order of seriousness: DEBUG < INFO < WARNING < ERROR < CRITICAL


# ---------------------------------------------------
# 💾 3. Saving logs to a file instead of the terminal
# ---------------------------------------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,  # needed because we already configured logging above
)

logging.info("This message goes into app.log, not the terminal")


# ---------------------------------------------------
# 🧑‍💻 4. A simple real example
# ---------------------------------------------------
def divide(a, b):
    logging.info(f"divide() called with a={a}, b={b}")
    result = a / b
    logging.info(f"Result was {result}")
    return result


divide(10, 2)


# ---------------------------------------------------
# 🆚 print() vs logging - why bother switching?
# ---------------------------------------------------
# print()                          logging
# ---------------------------------------------------------
# disappears when terminal closes   saved permanently to a file
# no timestamp                      auto-adds date & time
# no severity levels                DEBUG/INFO/WARNING/ERROR/CRITICAL
# hard to turn off everywhere       one line disables all logs
# fine for quick scripts            what real projects actually use


# ---------------------------------------------------
# 💡 Why does this matter for Data Science?
# ---------------------------------------------------
# When a data pipeline runs for hours and fails at 3 AM, print() statements
# are gone. A log file tells you exactly what happened and when - which
# step failed, what the input looked like, everything.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Calling logging.basicConfig() more than once in the same run without
# force=True - the second call gets silently ignored, and you'll be stuck
# wondering why your new settings "aren't working".
