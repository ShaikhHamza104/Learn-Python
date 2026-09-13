# 📚 Topic: Environment Setup & Tooling

Before writing Python code, establishing an isolated development workspace is essential. A virtual environment keeps your project dependencies self-contained and prevents package version conflicts between different projects on your computer. This chapter walks you through creating virtual environments with Python's built-in `venv`, leveraging the high-speed modern `uv` package manager, locking dependency versions, and configuring `.gitignore` to keep repositories clean.

---

## 📂 What's in this folder

| File | What it teaches |
|------|------------------|
| `01_venv_create.md` | How to create, activate, and deactivate isolated Python environments using standard `venv` across Windows, macOS, and Linux. |
| `02_uv_package_manager.md` | Using Astral's ultra-fast package installer and resolver `uv` to speed up dependency management. |
| `03_requirements_freeze.md` | Pinning and exporting reproducible package versions using `pip freeze` and `requirements.txt`. |
| `04_gitignore.md` | Preventing temporary bytecode, environment binaries, and sensitive credentials from polluting Git history. |

---

## 💡 Key points

1. **Always isolate your project**: Installing third-party packages globally can break system tools; always activate a project-specific virtual environment (`.venv/`) before running `pip install`.
2. **Reproducibility is non-negotiable**: Every collaborator needs identical package versions, which you share via a pinned `requirements.txt` file.
3. **Never commit `.venv` to Git**: Virtual environment folders contain thousands of platform-specific machine binaries; always exclude `.venv/` using your `.gitignore` file.

---

## 🧠 Beginner tip

Always check your terminal prompt before running code or installing libraries: if you see `(.venv)` prepended to your command line, your isolated environment is active and safe to use!

---

## 📊 Where this is used in Data Science

Data science and machine learning workflows depend on large ecosystems of libraries (such as NumPy, Pandas, Scikit-learn, and PyTorch) that require exact version alignment to avoid subtle calculation differences or GPU driver incompatibilities. Data teams rely on locked environments and containerization (like Docker) so that a machine learning model trained on a local workstation produces the exact same statistical results when deployed into production cloud pipelines.

---

## 🛠️ Code Examples

### 1. Creating and Activating a Virtual Environment (`venv`)
```bash
# Create the virtual environment
python -m venv .venv

# Activate on Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Activate on macOS / Linux
source .venv/bin/activate
```

### 2. High-Speed Workflows with `uv`
```bash
# Create an environment with uv
uv venv

# Install packages at lightning speed
uv pip install -r requirements.txt
```

### 3. Freezing and Installing Dependencies
```bash
# Save installed packages to requirements.txt
pip freeze > requirements.txt

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### 4. Basic `.gitignore` Rule
```gitignore
# Exclude the virtual environment folder from Git
.venv/
__pycache__/
*.pyc
```

---

## ⏭️ What's Next?
With a clean environment configured, you are ready to write your first program in **[Chapter 01 — Basics](../chapter_01_basics/README.md)**!