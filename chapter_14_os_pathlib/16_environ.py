"""
📚 Topic: Environment Variables (`os.environ`)

This script demonstrates reading and inspecting system environment variables
via `os.environ`.

💡 Key points:
    1️⃣ `os.environ` acts as a dictionary of system environment variables
    2️⃣ Safe lookup using `os.environ.get("KEY", default)`
    3️⃣ Storing configuration and API keys outside source code

🧠 Beginner tip:
    Never hardcode secrets or passwords in source code; retrieve them from
    environment variables instead.
"""


# importing os module : os module is a build in module
import os

# Assuming you have a PATH environment variable
path = os.environ["PATH"]
print(path)
