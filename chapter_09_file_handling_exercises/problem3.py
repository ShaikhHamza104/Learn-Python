"""
📚 Topic: Chapter 09 Exercise - Problem 3

Generate multiplication tables from 2 to 20 and write each table to a
dedicated text file.

💡 Key points:
    1️⃣ Generating arithmetic multiplication tables
    2️⃣ Writing files dynamically using formatted filenames
    3️⃣ Organizing generated output files in a subfolder
"""
import os


def generate_tables():
    script_dir = os.path.dirname(__file__)
    table_dir = os.path.join(script_dir, "table")
    os.makedirs(table_dir, exist_ok=True)

    for i in range(2, 21):
        table_path = os.path.join(table_dir, f"table_{i}.txt")
        with open(table_path, "w", encoding="utf-8") as f:
            for j in range(1, 11):
                f.write(f"{i} x {j} = {i * j}\n")


generate_tables()
