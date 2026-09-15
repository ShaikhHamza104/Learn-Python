"""
📚 Topic: JSON Serialization & Deserialization

This script demonstrates serializing Python data structures to JSON files and
deserializing JSON data back into Python objects.

💡 Key points:
    1️⃣ `json.dump(obj, f)`: serializes Python data to a file
    2️⃣ `json.load(f)`: deserializes JSON file content into Python dicts/lists
    3️⃣ `json.dumps()` / `json.loads()`: operate on in-memory strings

🧠 Beginner tip:
    JSON natively maps to Python primitives: JSON objects become dicts, arrays
    become lists, and booleans become True/False.
"""
# 🧩 Working with JSON files
# JSON = JavaScript Object Notation -> looks exactly like a Python dictionary
# It's the most common format for APIs, config files, and web data

import json

# ---------------------------------------------------
# ✍️ 1. Writing a JSON file (Python dict -> JSON file)
# ---------------------------------------------------
student = {
    "name": "Hamza",
    "age": 21,
    "course": "Data Science",
    "skills": ["Python", "SQL", "Pandas"],   # JSON supports lists too!
    "is_placed": False
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)      # indent=4 makes it human-readable

print("✅ student.json created!")


# ---------------------------------------------------
# 📖 2. Reading a JSON file (JSON file -> Python dict)
# ---------------------------------------------------
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])          # access it just like a normal dict
print(data["skills"][0])     # -> "Python"


# ---------------------------------------------------
# 🔄 3. Converting between JSON <-> string (this is what APIs actually send)
# ---------------------------------------------------
# dumps() = dict -> string (with an 's' for 'string')
json_string = json.dumps(student, indent=4)
print(json_string)
print(type(json_string))     # <class 'str'>

# loads() = string -> dict
back_to_dict = json.loads(json_string)
print(type(back_to_dict))    # <class 'dict'>


# ---------------------------------------------------
# 🆚 dump vs dumps (this trips up EVERYONE at first)
# ---------------------------------------------------
# json.dump()   -> writes directly to a FILE
# json.dumps()  -> converts to a STRING (the 's' stands for string)
# json.load()   -> reads directly from a FILE
# json.loads()  -> converts a STRING back to a dict


# ---------------------------------------------------
# 💡 Why does this matter for Data Science?
# ---------------------------------------------------
# When you call an API with the `requests` module, the response comes back
# as JSON. You'll use json.loads() (or response.json()) constantly to turn
# that raw data into something Python can actually work with.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Trying to json.dump() a dict that has non-JSON-friendly types inside it
# (like a datetime object) -> this throws "TypeError: Object of type
# datetime is not JSON serializable". Convert those to strings first.
