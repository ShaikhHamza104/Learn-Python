# 🚀 uv — The Fast Python Package Manager

## ❓ What is uv?

`uv` does everything `venv` + `pip` do — creating environments, installing packages, managing `requirements.txt` — but it's built in Rust and is **10-100x faster**. 🏎️

I use `uv` in most of my other repos now instead of plain `pip`, so this file exists to show you why.

## 📥 Installing uv (one-time only)

**Mac / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check it installed correctly:
```bash
uv --version
```

## 📦 Creating a project the uv way

```bash
# go inside your project folder
cd my_project

# create a virtual environment (way faster than python -m venv)
uv venv

# activate it (same as before)
source env/bin/activate      # Mac/Linux
env\Scripts\activate         # Windows
```

## ➕ Installing packages

Instead of `pip install pandas`:

```bash
uv pip install pandas
```

That's it — it's a drop-in replacement, just faster ⚡

## 🔒 Modern uv workflow (recommended)

`uv` also has its own project system that auto-manages a lockfile for you:

```bash
# start a new uv-managed project
uv init my_project
cd my_project

# add a package (this updates pyproject.toml automatically)
uv add pandas

# run your script inside the environment, no manual activation needed
uv run main.py
```

## 🆚 pip/venv vs uv — quick comparison

| Task | Old way (pip + venv) | New way (uv) |
|---|---|---|
| Create environment | `python -m venv env` | `uv venv` |
| Install a package | `pip install pandas` | `uv pip install pandas` |
| Add + track a package | manually edit `requirements.txt` | `uv add pandas` (automatic) |
| Run a script | activate, then `python main.py` | `uv run main.py` (no activation needed!) |
| Speed | 🐢 slow | ⚡ very fast |

## 🧠 Which one should you use?

- **Learning the fundamentals for the first time?** → do `01_venv_create.md` first so you understand what's actually happening under the hood.
- **Building real projects?** → switch to `uv`, it saves a ton of time.

## ⚠️ Common mistake

Mixing `pip` and `uv` in the same project can cause confusing dependency conflicts. Pick one per project and stick with it.

---
👉 Next up: `03_requirements_freeze.md` — how to save and share your dependencies with both tools