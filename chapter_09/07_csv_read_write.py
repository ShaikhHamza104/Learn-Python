"""
📚 Topic: CSV File Processing

This script demonstrates csv file processing using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for csv file processing
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how csv
    file processing affects the result.
"""

# 📊 Working with CSV files
# CSV = Comma Separated Values -> basically a simple spreadsheet saved as plain
# text
# Every row is a line, every value is separated by a comma

import csv

# ---------------------------------------------------
# ✍️ 1. Writing a CSV file
# ---------------------------------------------------
students = [
    ["Name", "Age", "Course"],  # header row
    ["Hamza", 21, "Data Science"],
    ["Ali", 22, "Web Dev"],
    ["Sara", 20, "AI/ML"],
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)  # writes all rows at once

print("✅ students.csv created!")


# ---------------------------------------------------
# 📖 2. Reading a CSV file (basic way - rows as lists)
# ---------------------------------------------------
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)  # each row comes back as a list, e.g. ['Hamza', '21',
        # 'Data Science']


# ---------------------------------------------------
# 📖 3. Reading a CSV file (better way - rows as dictionaries)
# ---------------------------------------------------
# DictReader automatically uses the first row as keys
# this is way more readable than row[0], row[1]...
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        message = f"{row['Name']} is {row['Age']} years old and studies "
        print(message + f"{row['Course']}")


# ---------------------------------------------------
# ➕ 4. Appending a new row (without deleting old data)
# ---------------------------------------------------
new_student = ["Zoya", 23, "Data Analytics"]

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)  # note: writerow (singular) for ONE row

print("✅ Zoya added to students.csv")


# ---------------------------------------------------
# 💡 Why does this matter for Data Science?
# ---------------------------------------------------
# Almost every dataset you'll ever download starts as a CSV file.
# Before you even touch pandas, you should know how Python reads one
# manually - it makes pandas.read_csv() feel way less "magic" later.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Forgetting newline="" when opening the file on Windows
# -> this causes an extra blank line between every row
# always write: open("file.csv", "w", newline="")
