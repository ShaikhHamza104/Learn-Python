"""
📚 Topic: 08 Rename

This script demonstrates 08 rename using exception handling and imports.

💡 Key points:
    1️⃣ the basic syntax for 08 rename
    2️⃣ how exception handling fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    08 rename affects the result.
"""

# importing os module : os module is a build in module
import os

try:
    # Renames a file or directory

    os.rename("notes", "Python notes")
# If Source is a file
# but destination is a directory
except IsADirectoryError:
    print("Source is a file but destination is a directory.")

# If source is a directory
# but destination is a file
except NotADirectoryError:
    print("Source is a directory but destination is a file.")

# For permission related errors
except PermissionError:
    print("Operation not permitted.")

# For other errors
except OSError as error:
    print(error)

except Exception:
    print("Some other error are occer you coud not hande this error ")
