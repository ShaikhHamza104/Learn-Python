# 📦 Saving Your Python Dependencies

So your project works perfectly on your computer. Great! 😎

But what happens when you:
- move the project to another computer 💻
- share it with a friend 👨‍💻
- upload it to GitHub 🐙
- deploy it to a server ☁️
- come back to the project after a few months? 🤔

You need a way to tell Python:

> "These are the packages my project needs."

That's where dependency files come in. 📋

---

## ❓ What are dependencies?

A **dependency** is a package that your project needs to work.

For example, if your project uses:

```python
import pandas
import numpy
import matplotlib
```

then your project depends on:
- `pandas`
- `numpy`
- `matplotlib`

Instead of asking someone to install packages one by one, we can save the list in a file.

📄 Usually this file is called:

```text
requirements.txt
```

---

# 📝 Creating `requirements.txt`

If you are using the traditional `pip + venv` workflow, first activate your environment:

**Windows:**

```powershell
env\Scripts\activate
```

**Mac / Linux:**

```bash
source env/bin/activate
```

Then run:

```bash
pip freeze > requirements.txt
```

This creates a file like:

```text
requirements.txt
```

Inside it, you may see:

```text
numpy==2.3.2
pandas==2.3.1
matplotlib==3.10.5
scikit-learn==1.7.1
```

The `==` means that a specific version is being recorded.

For example:

```text
pandas==2.3.1
```

means:

> Install pandas version 2.3.1.

---

# 📥 Installing from `requirements.txt`

Now imagine your friend downloads your project.

They don't need to manually install every package.

They can simply run:

```bash
pip install -r requirements.txt
```

And pip will install the packages listed in the file. 🚀

### Complete example

```bash
# create environment
python -m venv env

# activate environment

# Windows
env\Scripts\activate

# install everything from requirements.txt
pip install -r requirements.txt
```

That's much easier than installing packages one by one.

---

# 🚀 What about uv?

If you are using the modern `uv` project workflow, you normally don't need to manually maintain `requirements.txt`.

A typical uv project uses:

```text
pyproject.toml
uv.lock
```

### `pyproject.toml`

This contains information about your project and its direct dependencies.

For example:

```toml
dependencies = [
    "numpy",
    "pandas",
    "scikit-learn"
]
```

### `uv.lock`

This records the exact dependency versions and other information needed to reproduce the environment.

Think of it like this:

```text
pyproject.toml
       ↓
"What does my project need?"

uv.lock
       ↓
"Exactly what versions should be installed?"
```

---

# ➕ Adding a package with uv

Instead of:

```bash
uv pip install pandas
```

for a uv-managed project, you can use:

```bash
uv add pandas
```

This updates your project configuration and lock file automatically. 🔒

You can add multiple packages:

```bash
uv add numpy pandas matplotlib scikit-learn
```

Then run your project with:

```bash
uv run main.py
```

---

# 🔄 Updating dependencies

With a traditional `requirements.txt` workflow, you may need to update the file when you install or change packages.

For example:

```bash
pip install requests
```

Then update the requirements file:

```bash
pip freeze > requirements.txt
```

⚠️ Be careful with this command.

`pip freeze` records **everything installed in the environment**, not just the packages you personally chose for your project.

This is one reason modern project tools such as `uv` can be more convenient.

---

# 🆚 requirements.txt vs uv

| Task | pip + requirements.txt | uv project |
|---|---|---|
| Dependency file | `requirements.txt` | `pyproject.toml` |
| Lock file | Usually not used | `uv.lock` |
| Add package | `pip install pandas` | `uv add pandas` |
| Install requirements | `pip install -r requirements.txt` | `uv sync` |
| Run project | `python main.py` | `uv run main.py` |
| Dependency management | Manual | More automatic |

---

# 🧠 Which should you use?

### If you're learning Python basics:

```text
venv + pip + requirements.txt
```

is worth understanding.

It teaches you the fundamentals. 👍

### For your real projects:

```text
uv + pyproject.toml + uv.lock
```

is a cleaner modern workflow.

You should understand both, but you don't need to use both in the same project.

---

# ⚠️ Common mistakes

### ❌ Mistake 1: Forgetting to activate the environment

You might accidentally install packages into your global Python installation.

Check your terminal first.

You should see something like:

```text
(env)
```

---

### ❌ Mistake 2: Using the wrong requirements file

Make sure you are running:

```bash
pip install -r requirements.txt
```

from the folder where `requirements.txt` exists.

---

### ❌ Mistake 3: Mixing package managers without understanding them

Using:

```text
pip
uv pip
uv add
```

randomly in the same project can make dependency management confusing.

Pick a workflow and understand how it works.

---

# 🧠 Quick recap

| Command | What it does |
|---|---|
| `pip freeze` | Shows installed packages |
| `pip freeze > requirements.txt` | Saves installed packages |
| `pip install -r requirements.txt` | Installs saved packages |
| `uv add pandas` | Adds pandas to a uv project |
| `uv sync` | Creates/updates the uv environment |
| `uv run main.py` | Runs your project using uv |

---

## 🎯 The main idea

Don't think of `requirements.txt` as "just another file."

Think of it as:

> 📋 A shopping list of Python packages needed by your project.

And with uv:

> `pyproject.toml` + `uv.lock` provide a more modern way to manage those dependencies.

---

👉 Next up: `04_gitignore.md` — what you should NEVER upload to GitHub.
