# 📚 Topic: Object-Oriented Programming (OOP) Practice (Exercises)

Hands-on exercises applying OOP fundamentals: modeling company records with class attributes and methods, implementing a multi-operation calculator class with mathematical transformations, inspecting class vs. instance attribute resolution, and augmenting classes with `@staticmethod` decorators.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Defines a `Programmer` class with company class attributes and a method that prints formatted profiles for employees. |
| `problem2.py` | Implements a `Calculator` class with methods to calculate squares (`n**2`), cubes (`n**3`), and square roots using `math.sqrt()`. |
| `problem3.py` | Demonstrates attribute lookup hierarchy on class `A` when accessing class attribute `a = 10` through an object instance. |
| `problem4.py` | Extends the `Calculator` class by adding a static greeting method (`@staticmethod def greete()`). |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: Demonstrates encapsulation by grouping related attributes (`comany`, employee list) and iteration logic inside a single `Programmer` class.
2. **Problem 2 (`problem2.py`)**: Uses class methods with `self` and parameters to perform calculations like power and `math.sqrt()`.
3. **Problem 3 (`problem3.py`)**: Verifies that accessing an attribute on an instance (`o.a`) falls back to the class attribute when no instance attribute of the same name exists.
4. **Problem 4 (`problem4.py`)**: Uses `@staticmethod` to attach utility behavior to a class without needing access to instance state (`self`) or class state (`cls`).

## 🧠 Beginner tip

Use `@staticmethod` when a function logically belongs inside a class namespace (like a greeting or math utility), but does not need to inspect or modify any attributes on `self` or `cls`.

## 📊 Where this is used in Data Science

Classes like `Calculator` mirror data transformation utilities in data science. For example, custom feature scalers or mathematical transformers in scikit-learn subclass `BaseEstimator` and implement `.transform()` and `.fit()`, encapsulating power transforms, logarithms, and square roots into reusable pipeline components.

## 🏃 How to Run Each Exercise

Run each exercise script from your terminal:

```bash
python problem1.py
python problem2.py
python problem3.py
python problem4.py
```

## 📖 Related Lessons

- [Chapter 10 - Object-Oriented Programming](../chapter_10_oop/README.md)

## ⏭️ What's Next

- [Chapter 11 - Inheritance and Polymorphism](../chapter_11_inheritance_polymorphism/README.md)
