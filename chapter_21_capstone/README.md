# 🎓 Chapter 21 — Capstone Project

This is it — the final chapter! 🏁

No more lessons here. A capstone means **you build a real project yourself**, using everything you learned from Chapter 1 to Chapter 20. This is where all the small pieces come together.

> 💬 Think of it like this: chapters 1–20 taught you the words and grammar. Now you write your own story.

---

## 📂 What's in this folder?

| File              | Purpose                                      |
|-------------------|----------------------------------------------|
| `main.py`         | Your project code goes here                  |
| `requirements.txt`| List of external packages your project needs |
| `README.md`       | This file — describe your project in it      |

---

## 🧠 Skills you can use now

By this point, you know how to:

- ✅ use variables, strings, numbers, and user input
- 📋 work with lists, tuples, dictionaries, and sets
- 🔀 make decisions with `if / elif / else`
- 🔁 repeat work with `for` and `while` loops
- 🧩 write functions and handle errors safely
- 📄 read and write files
- 🏗️ use classes, objects, and inheritance
- 📦 import modules and packages
- 🌐 fetch data from APIs
- 🔍 use regex, iterators, generators, and functional tools

A good capstone combines **at least 4–5** of these.

### 🗺️ Chapter map — where to review each skill

Stuck on something while building? Jump back to the chapter that teaches it:

| Skill                        | Review in                                      |
|------------------------------|-------------------------------------------------|
| Input, printing, variables   | [chapter_02/](../chapter_02)                    |
| Strings & formatting         | [chapter_03/](../chapter_03)                    |
| Lists, tuples                | [chapter_04/](../chapter_04)                    |
| Dicts & sets                 | [chapter_05/](../chapter_05)                    |
| if / elif / else             | [chapter_06/](../chapter_06)                    |
| Loops                        | [chapter_07/](../chapter_07)                    |
| Functions                    | [chapter_08/](../chapter_08)                    |
| Files (txt, CSV, JSON)       | [chapter_09/](../chapter_09)                    |
| Classes & OOP                | [chapter_10/](../chapter_10), [chapter_11/](../chapter_11) |
| Exceptions & logging         | [chapter_12/](../chapter_12)                    |
| Modules & packages           | [chapter_13/](../chapter_13)                    |
| Working with the OS          | [chapter_14/](../chapter_14)                    |
| Regex                        | [chapter_15_regex/](../chapter_15_regex)        |
| Collections                  | [chapter_16_collections/](../chapter_16_collections) |
| Generators                   | [chapter_17_iterators_generators/](../chapter_17_iterators_generators) |
| Itertools                    | [chapter_18_itertools/](../chapter_18_itertools) |
| Decorators, functools        | [chapter_19_functional_tools/](../chapter_19_functional_tools) |
| APIs & JSON data             | [chapter_20_apis_and_data/](../chapter_20_apis_and_data) |

---

## 💡 Project ideas (pick one or invent your own)

| Project              | What it practices                          |
|----------------------|--------------------------------------------|
| 📝 To-Do App         | file handling, functions, loops            |
| 💰 Expense Tracker   | dictionaries, file saving, reports         |
| ❓ Quiz Game         | loops, conditions, score tracking           |
| 🌦️ Weather CLI       | APIs, error handling, parsing JSON          |
| 🎮 Text Adventure    | OOP, functions, control flow               |
| 🔐 Password Manager  | file handling, regex, string methods       |
| 📚 Library System    | classes, inheritance, searching, sorting   |

Pick something **you** actually want to use — that keeps you motivated. 🚀

---

## 🛠️ How to build it

1. **Pick an idea** from the list above (or your own)
2. **Write it down** — what does the app do? what does the user see?
3. **Start small** — make the simplest version work first
4. **Add features one by one** — save to a file, add a class, handle errors
5. **Test it** — break it on purpose, then fix it

### 🧱 Suggested structure

Keep it simple — one folder, a few files. For example, a To-Do app could look like:

```text
chapter_21_capstone/
├── main.py          # menu + starts the app
├── storage.py       # load/save tasks (you'd create this)
├── tasks.py         # add/delete/complete logic (you'd create this)
├── requirements.txt
└── README.md
```

You don't need classes for a small CLI app — functions are fine. Use classes only if they genuinely make your code clearer.

### 🎯 Milestones

Tick these off as you go:

- [ ] **M1 — Skeleton:** menu shows, user can pick an option, loops until "quit"
- [ ] **M2 — Core feature:** the main feature works (in memory)
- [ ] **M3 — Persistence:** data survives after restart (file/JSON)
- [ ] **M4 — Safety:** bad input handled with try/except, no crashes
- [ ] **M5 — Polish:** comments, clean output, final README

### ▶️ Run your project

```bash
python main.py
```

### 📦 If you use external packages

Add them to `requirements.txt` like this:

```text
requests
rich
```

Then install with:

```bash
pip install -r requirements.txt
```

---

## ✅ Definition of done

Your capstone is complete when:

- [ ] it runs without crashing on normal input
- [ ] it uses at least 4–5 concepts from the list above
- [ ] it handles at least one bad input without dying (try/except 👀)
- [ ] the code has comments explaining your choices
- [ ] you can demo it to someone in under 2 minutes

### 🧪 Quick test ideas

Before calling it done, try these on YOUR app:

- Enter a number where text is expected
- Press Enter without typing anything
- Pick an invalid menu option (like 99)
- Run it twice in a row — does saved data come back?

If it survives all four, you built something solid. 💪

---

## 📝 Document your project

When you're done, replace this README with a short description of YOUR project:

- what it does
- how to run it
- what you learned while building it

---

## 🏆 Final words

You started with `print("Hello, world!")`.

Now you're building whole projects on your own. That's real progress — take a minute to appreciate it. 🐍✨

> Every programmer you admire once sat where you are now. The difference is they kept building. Keep building. 💪
