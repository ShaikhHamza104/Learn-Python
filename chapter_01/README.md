# 🐍 Chapter 01 — Your First Python Program

> ✏️ In this chapter, you'll write your very first line of Python, learn what modules are, and understand why comments matter. Let's go!

---

## 📂 What's Inside This Folder?

| #  | File                    | Topic                          |
|----|-------------------------|--------------------------------|
| 01 | `01_hello_world.py`     | 👋 Printing your first message |
| 02 | `02_module_example.py`  | 📦 Using an external module    |
| 03 | `02_comment_example.py` | 💬 Writing comments in Python  |

---

## 👋 01 — Hello World (`01_hello_world.py`)

This is the classic first program every programmer writes. Seriously — everyone starts here.

```python
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
```

### 🔍 What's going on?

- `print()` → Shows text on your screen. That's it. Simple.
- `def main():` → We put our code inside a function called `main`. Think of it like a recipe — you write the steps, then run them.
- `if __name__ == "__main__":` → This line says *"only run this if I double-click this file directly"*. Don't stress about it now, you'll understand it better later.

### ▶️ How to run it

```bash
python 01_hello_world.py
```

**Output:**
```
Hello, world!
```

That's it — you just ran Python! 🎉

### 🧪 Try changing it

Open the file and change the text inside `print()`:

```python
print("Hey, I'm learning Python!")
print("My name is Hamza")
print("Let's gooo 🚀")
```

Run it again and see your new messages. Play around — you can't break anything here.

---

## 📦 02 — Modules (`02_module_example.py`)

Modules = code someone else already wrote so you don't have to.

```python
import pyjokes

def print_joke():
    joke_text = pyjokes.get_joke()
    print(joke_text)

if __name__ == "__main__":
    print_joke()
```

### 🔍 Line-by-line breakdown

| Line | What it does |
|------|-------------|
| `import pyjokes` | Loads the `pyjokes` module (a library of programming jokes) |
| `pyjokes.get_joke()` | Grabs a random joke from the library |
| `joke_text = ...` | Stores that joke in a variable (a named box) |
| `print(joke_text)` | Shows the joke on screen |

### ▶️ How to run it

First, install the dependency:

```bash
uv sync
```

Then run:

```bash
python 02_module_example.py
```

Run it 3-4 times — you'll get a different joke each time 😄

### 💡 What is a module, really?

Think of it this way:

- You **could** bake bread from scratch every time 🍞
- Or you **could** just buy bread from a bakery

Modules are the bakery. Someone already did the hard work. You just `import` their code and use it.

Python has **thousands** of modules for everything — math, web, games, AI, you name it.

### 📌 Common built-in modules you'll use later

| Module    | What it does              |
|-----------|--------------------------|
| `math`    | Math stuff (sqrt, pi...) |
| `random`  | Random number generation |
| `os`      | Work with files/folders  |
| `datetime`| Dates and times          |

You don't need to install these — they come with Python!

---

## 💬 03 — Comments (`02_comment_example.py`)

Comments are notes **for humans**. Python completely ignores them.

### 📝 Single-line comments → use `#`

```python
# This line is a comment — Python skips it
print("Hello")   # This part after # is also a comment
```

### 📝 Multi-line comments → use `"""` or `'''`

```python
"""
This is a multi-line comment.
Good for longer explanations.
Python ignores this too.
"""
```

### 🤷 Why bother with comments?

Imagine you write code today. You come back 2 months later and think:

> *"What was I doing here...?"* 😵💫

Comments save future-you. They explain:

- **What** something does
- **Why** you did it that way

### ✅ Good vs ❌ Bad comments

```python
# ❌ Bad — too obvious, we can see that
x = 5  # Set x to 5

# ✅ Good — explains the WHY
max_retries = 5  # Stop after 5 tries to avoid infinite loop
```

### 🔥 Pro tip: Commenting out code

Want to temporarily stop a line from running? Just add `#` in front:

```python
# print("This won't run")
print("This WILL run")
```

Super useful when you're debugging!

---

## 📋 Quick Recap

| Concept   | What you learned |
|-----------|-----------------|
| `print()` | Display text on screen |
| `import`  | Load a module (someone else's code) |
| `#`       | Single-line comment |
| `""" """`  | Multi-line comment / docstring |
| `def`     | Define a function |

---

## 🏋️ Practice — Try These Before Moving On

1. **Change the greeting** → Edit `01_hello_world.py` to print 3 lines about yourself
2. **Joke collector** → Run `02_module_example.py` five times and pick your favorite joke
3. **Comment your code** → Open any file and add your own comments explaining each line in your own words
4. **Try a built-in module** → Write a small script using `random`:
   ```python
   import random
   print(random.randint(1, 100))  # prints a random number between 1 and 100
   ```

---

## ⏭️ What's Next?

**[Chapter 02 — Variables & Data Types →](../chapter_02/README.md)**

You'll learn how to store information (numbers, text, etc.), take input from users, and do calculations.

---

## 🔗 Helpful Links

- 🐍 [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- 📖 [Automate the Boring Stuff (free book)](https://automatetheboringstuff.com/)
- 🎓 [Python for Everybody (free course)](https://www.py4e.com/)

---

> 💬 *Stuck? Read the error message first — Python usually tells you what went wrong. Still stuck? Google the error. Every programmer does this, even the pros.* ✌️
