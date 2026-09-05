# 🐍 Virtual Environments (venv)

## ❓ What is a virtual environment?

Think of it like a **separate box** for each of your Python projects.

Without one, every package you install (`pip install pandas`) gets dumped into your ONE global Python — and different projects can need different, clashing versions of the same package. A venv gives each project its own isolated box so nothing clashes. 📦

## ✅ Creating a venv (built into Python, no install needed)

```bash
# go inside your project folder first
cd my_project

# create the environment (this creates a folder called "env")
python -m venv env
```

## ▶️ Activating it

You have to activate the environment every time you open a new terminal to work on the project.

**Windows:**
```bash
env\Scripts\activate
```

**Mac / Linux:**
```bash
source env/bin/activate
```

When it's active, you'll see `(env)` show up at the start of your terminal line — that's how you know it worked ✅

## ⏹️ Deactivating

```bash
deactivate
```

## 🧠 Quick recap

| Command | What it does |
|---|---|
| `python -m venv env` | creates the environment |
| `env\Scripts\activate` (Win) | turns it on |
| `source env/bin/activate` (Mac/Linux) | turns it on |
| `deactivate` | turns it off |

## ⚠️ Common mistake

Installing packages BEFORE activating the venv — they'll go to your global Python instead of the project. Always activate first, install second.

---
👉 Next up: there's a faster, modern alternative to all of this called **uv** — check `02_uv_package_manager.md`