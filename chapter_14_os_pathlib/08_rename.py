"""
📚 Topic: Renaming and Moving Files (`os.rename()`)

This script demonstrates renaming or moving files across filesystem paths
using `os.rename()`.

💡 Key points:
    1️⃣ Changing filename or moving across directories
    2️⃣ Atomic file replacement on POSIX systems
    3️⃣ Handling `FileNotFoundError` and `FileExistsError`

🧠 Beginner tip:
    For moving files across different drives or filesystems, prefer
    `shutil.move()`.
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
