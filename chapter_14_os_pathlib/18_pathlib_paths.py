"""
📚 Topic: 18 Pathlib Paths

This script demonstrates 18 pathlib paths using for loops, conditions, file
or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for 18 pathlib paths
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    18 pathlib paths affects the result.
"""


# 🗂️ pathlib - the modern replacement for the os module
#
# Earlier in this chapter you used os.getcwd(), os.mkdir(), os.rename(),
# os.remove() etc. This file shows the SAME tasks done the pathlib way.
# os still works fine - but pathlib is what most new code uses today.

from pathlib import Path

# ---------------------------------------------------
# 📍 1. os.getcwd()  ->  Path.cwd()
# ---------------------------------------------------
# old:  import os
#       os.getcwd()
current_dir = Path.cwd()
print("Current directory:", current_dir)


# ---------------------------------------------------
# 📁 2. os.mkdir()  ->  Path.mkdir()
# ---------------------------------------------------
# old:  os.mkdir("new_folder")   <- crashes if folder already exists!
new_folder = Path("new_folder")
new_folder.mkdir(exist_ok=True)  # exist_ok=True stops it from crashing
print("✅ Folder created (or already existed)")


# ---------------------------------------------------
# ✏️ 3. os.rename()  ->  Path.rename()
# ---------------------------------------------------
sample_file = Path("new_folder/sample.txt")
sample_file.write_text("hello!")  # create a quick file to rename

renamed_file = sample_file.rename("new_folder/renamed_sample.txt")
print("✅ Renamed to:", renamed_file)


# ---------------------------------------------------
# 🗑️ 4. os.remove()  ->  Path.unlink()
# ---------------------------------------------------
# old:  os.remove("file.txt")
# note: pathlib calls it unlink(), not remove() - a bit confusing at first!
renamed_file.unlink()
print("✅ File deleted")


# ---------------------------------------------------
# 📂 5. os.listdir()  ->  Path.iterdir()
# ---------------------------------------------------
# old:  os.listdir("new_folder")   <- gives back plain strings
# new:  gives back full Path objects, which is more useful
for item in new_folder.iterdir():
    print("Found:", item)


# ---------------------------------------------------
# 🌍 6. os.environ  ->  still the same in pathlib (no change here)
# ---------------------------------------------------
# pathlib is only about FILES and FOLDERS, not environment variables
# so for env vars you'll still reach for os.environ, that's normal


# ---------------------------------------------------
# 🔗 7. os.path.join()  ->  the / operator
# ---------------------------------------------------
# old:  os.path.join("data", "students.csv")   <- easy to mess up on Windows
# new:
file_path = Path("data") / "students.csv"
print("Joined path:", file_path)


# ---------------------------------------------------
# 🆚 Full side-by-side cheat sheet
# ---------------------------------------------------
# os module                          pathlib
# ---------------------------------------------------------
# os.getcwd()                        Path.cwd()
# os.mkdir("folder")                 Path("folder").mkdir()
# os.rename(old, new)                Path(old).rename(new)
# os.remove("file.txt")              Path("file.txt").unlink()
# os.listdir("folder")               Path("folder").iterdir()
# os.path.join("a", "b")             Path("a") / "b"
# os.path.exists(path)               Path(path).exists()
# os.path.isfile(path)               Path(path).is_file()
# os.path.isdir(path)                Path(path).is_dir()


# ---------------------------------------------------
# 💡 Why does this matter for Data Science?
# ---------------------------------------------------
# pathlib code looks the same on Windows, Mac, and Linux - important
# when you're sharing notebooks/scripts with teammates or deploying to
# a server. os.path string-joining breaks more easily across systems.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Trying to os.remove() a Path object directly - os functions expect
# plain strings sometimes. If you get a weird error, wrap it: str(path)
# Or better - just stick to the pathlib method (.unlink()) instead of
# mixing os functions with Path objects.
