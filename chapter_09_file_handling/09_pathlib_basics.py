"""
📚 Topic: Modern Path Handling with `pathlib`

This script demonstrates object-oriented filesystem path manipulation using
Python's standard `pathlib.Path`.

💡 Key points:
    1️⃣ Creating cross-platform paths with `Path()`
    2️⃣ Composing paths cleanly using the `/` slash operator
    3️⃣ Convenient methods: `.exists()`, `.is_file()`, `.read_text()`

🧠 Beginner tip:
    `pathlib` replaces legacy `os.path` functions with clean, object-oriented
    methods that work seamlessly across Windows, macOS, and Linux.
"""
# 🗂️ Working with pathlib
# pathlib is the MODERN way to handle file paths in Python
# It replaces a lot of the old os.path string-joining mess from
# chapter_14_os_pathlib

from pathlib import Path

# ---------------------------------------------------
# 📍 1. Getting the current working directory
# ---------------------------------------------------
current_dir = Path.cwd()
print("Current folder:", current_dir)


# ---------------------------------------------------
# 🔗 2. Building paths (no more messy string + "/" + string)
# ---------------------------------------------------
# old os way:  path = "data" + "/" + "students.csv"   <- breaks on Windows!
# pathlib way (uses / like a normal division sign, works on ALL systems):
file_path = Path("data") / "students.csv"
print("File path:", file_path)


# ---------------------------------------------------
# 📄 3. Checking if a file/folder exists
# ---------------------------------------------------
if file_path.exists():
    print("✅ File exists!")
else:
    print("❌ File not found")


# ---------------------------------------------------
# 📁 4. Creating a folder (if it doesn't already exist)
# ---------------------------------------------------
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)  # exist_ok=True -> won't crash if it's
# already there
print("✅ 'data' folder ready")


# ---------------------------------------------------
# 📖 5. Reading/writing a file the pathlib way (shorter than open()!)
# ---------------------------------------------------
notes_file = Path("notes.txt")

notes_file.write_text("Learning pathlib today 🐍")  # no need for "with"
content = notes_file.read_text()
print(content)


# ---------------------------------------------------
# 🔍 6. Listing all files in a folder
# ---------------------------------------------------
for item in data_folder.iterdir():
    print("Found:", item.name)


# ---------------------------------------------------
# 🔎 7. Useful path info
# ---------------------------------------------------
print("File name:", file_path.name)  # students.csv
print("File extension:", file_path.suffix)  # .csv
print("Parent folder:", file_path.parent)  # data
print("Is a file?", file_path.is_file())
print("Is a folder?", data_folder.is_dir())


# ---------------------------------------------------
# 🆚 pathlib vs old os module (from chapter_14_os_pathlib)
# ---------------------------------------------------
# os.path.join("data", "students.csv")   ->   Path("data") / "students.csv"
# os.getcwd()                            ->   Path.cwd()
# os.path.exists(path)                   ->   Path(path).exists()
# os.mkdir("data")                       ->   Path("data").mkdir()
# os still works fine, but pathlib reads cleaner and is the current standard


# ---------------------------------------------------
# 💡 Why does this matter for Data Science?
# ---------------------------------------------------
# Every data project juggles folders full of raw data, cleaned data, and
# output files. pathlib makes managing all of that MUCH less painful,
# especially when your script needs to run on both Windows and Mac/Linux.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Forgetting that Path objects aren't plain strings - some old libraries
# expect a string. Fix it with str(file_path) if you ever get a type error.
