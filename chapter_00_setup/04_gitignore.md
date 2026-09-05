# 🚫 `.gitignore` — What NOT to Upload to GitHub

Git is great. 🐙

It helps us track our code and upload projects to GitHub.

But there is one important rule:

> ❌ Don't upload everything in your project folder.

Some files are unnecessary.

Some files can be huge.

And some files can contain **private information**. 🔐

That's where `.gitignore` comes in.

---

# ❓ What is `.gitignore`?

`.gitignore` is a special file that tells Git:

> "Ignore these files and folders."

For example:

```text
.venv/
.env
__pycache__/
```

Git will then avoid tracking these files.

---

# 🐍 Why ignore the virtual environment?

When you create a virtual environment:

```bash
uv venv
```

or:

```bash
python -m venv env
```

Python creates a folder containing installed packages and environment files.

For example:

```text
my_project/
│
├── .venv/
├── main.py
├── pyproject.toml
└── README.md
```

You normally **do not upload `.venv/` to GitHub**.

Why?

Because it can be large and it is not necessary.

Your project should contain the information needed to recreate the environment instead.

For a uv project, that usually means:

```text
pyproject.toml
uv.lock
```

---

# 🔐 Never upload `.env`

This is extremely important.

A `.env` file is often used for private values such as:

```text
API_KEY=your_secret_key
DATABASE_PASSWORD=your_password
SECRET_KEY=your_secret
```

If you upload this file to a public GitHub repository, someone else may be able to use those secrets. 😬

So add:

```text
.env
```

to `.gitignore`.

---

# 🗑️ What should you usually ignore?

A simple Python project may have:

```text
.venv/
venv/
env/

__pycache__/
*.py[cod]

.env

.ipynb_checkpoints/

.pytest_cache/

.coverage

.DS_Store
Thumbs.db
```

Let's understand them.

---

# 📁 Virtual environments

```text
.venv/
venv/
env/
```

These folders contain your local Python environment.

Don't upload them.

---

# 🐍 Python cache files

Python can create folders such as:

```text
__pycache__/
```

You may also see files such as:

```text
example.cpython-313.pyc
```

These are generated automatically by Python.

You don't need to upload them.

So:

```text
__pycache__/
*.py[cod]
```

can be ignored.

---

# 🔐 Environment files

```text
.env
```

This is one of the most important entries.

It may contain:

- API keys 🔑
- passwords 🔐
- database credentials 🗄️
- secret tokens 🎫
- private configuration

Never commit real secrets to GitHub.

---

# 📓 Jupyter Notebook checkpoints

If you use Jupyter Notebook, you may see:

```text
.ipynb_checkpoints/
```

These are automatically generated files.

Usually, you don't need them in Git.

So add:

```text
.ipynb_checkpoints/
```

---

# 💻 Operating system files

Different operating systems create unnecessary files.

For example:

```text
.DS_Store
```

is commonly created by macOS.

Windows may create:

```text
Thumbs.db
```

You generally don't need these in your repository.

---

# 📄 A simple Python `.gitignore`

For a beginner Python project, you can start with:

```gitignore
# =========================
# Python
# =========================

__pycache__/
*.py[cod]

# =========================
# Virtual environments
# =========================

.venv/
venv/
env/

# =========================
# Environment variables
# =========================

.env

# =========================
# Jupyter
# =========================

.ipynb_checkpoints/

# =========================
# Testing / coverage
# =========================

.pytest_cache/
.coverage
htmlcov/

# =========================
# Operating system files
# =========================

.DS_Store
Thumbs.db
```

Save this file as:

```text
.gitignore
```

Notice the `.` at the beginning.

It is:

```text
.gitignore
```

NOT:

```text
gitignore.txt
```

---

# 🔍 How to check what Git sees

Run:

```bash
git status
```

Git will show you files that are not being ignored.

For example:

```text
Untracked files:

    main.py
    README.md
    pyproject.toml
```

If `.env` or `.venv/` doesn't appear, that's usually a good sign. ✅

---

# ⚠️ Important: `.gitignore` does NOT delete files

This is a common beginner misunderstanding.

If you write:

```gitignore
.env
```

Git doesn't delete `.env`.

It simply tells Git:

> "Don't track this file."

The file still exists on your computer.

---

# 🚨 Important security warning

`.gitignore` is **not a magic security system**.

For example, imagine you accidentally commit:

```text
.env
```

and then add `.env` to `.gitignore`.

That does **not automatically remove the secret from Git history**.

If a real API key, password, or token has already been pushed to GitHub:

1. 🔴 Treat the secret as exposed.
2. 🔄 Revoke or rotate the secret.
3. 🧹 Remove it from the repository/history properly.

The safest rule is simple:

> **Never commit secrets in the first place.**

---

# 📦 What SHOULD go to GitHub?

A normal Python project might look like:

```text
my_project/
│
├── src/
│   └── main.py
│
├── tests/
│
├── .gitignore
├── README.md
├── pyproject.toml
└── uv.lock
```

These files are useful because another developer can understand and recreate the project.

---

# ❌ What usually should NOT go to GitHub?

```text
.venv/
.env
__pycache__/
.pytest_cache/
```

And don't blindly upload huge generated files or local data that the project doesn't need.

---

# 🧠 Quick recap

| File / Folder | Upload? | Why |
|---|---:|---|
| `.venv/` | ❌ | Local environment |
| `env/` | ❌ | Local environment |
| `.env` | ❌ | May contain secrets |
| `__pycache__/` | ❌ | Python-generated cache |
| `.pytest_cache/` | ❌ | Test cache |
| `README.md` | ✅ | Project documentation |
| `pyproject.toml` | ✅ | Project configuration |
| `uv.lock` | ✅ | Locked dependencies |
| `.gitignore` | ✅ | Tells Git what to ignore |
| `main.py` | ✅ | Your source code |

---

# 🎯 The main idea

Your GitHub repository should contain:

> 🧠 The important parts of your project.

Not:

> 🗑️ Every file that happens to exist on your computer.

A clean repository is easier to understand, share, maintain, and deploy.

---

## 🚀 Chapter 00 complete!

You now know:

- 🐍 How virtual environments work
- 🚀 How to use `uv`
- 📦 How dependencies are managed
- 🔒 How dependency files work
- 🚫 What `.gitignore` does
- 🔐 Why secrets should never be committed

You're ready to start writing actual Python code. 💪

👉 **Next chapter: Python Basics 🐍**
