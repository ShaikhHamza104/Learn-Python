"""
📚 Topic: File Modification Timestamps (`os.path.getmtime()`)

This script demonstrates reading file modification epoch timestamps and
formatting them into human-readable datetime strings.

💡 Key points:
    1️⃣ Retrieving modification timestamp as seconds since Unix epoch
    2️⃣ Converting epoch float to human date using `datetime.fromtimestamp()`
    3️⃣ Comparing file ages and detecting changes

🧠 Beginner tip:
    Use `time.ctime(os.path.getmtime(path))` for a quick formatted timestamp
    string.
"""


# importing os module : os module is a build in module
import os

# Returns the last modification time of a file
a = os.path.getmtime("15_getmtime.py")
print(a)  # 1723709371.0314808
