# 📚 Topic: Inheritance and Polymorphism Practice (Exercises)

Hands-on exercises applying inheritance hierarchies, constructor chaining with `super()`, multilevel class derivation (`Animals -> Pets -> Dog`), property getters and setters for salary increment calculations, and operator overloading (`__add__`, `__mul__`, `__str__`, `__len__`) across custom complex numbers and multi-dimensional vectors.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Extends a 2D vector class `TwoDVector` into `ThreeDVector` by chaining constructors with `super().__init__()` and adding dimension `k`. |
| `problem2.py` | Models a multilevel inheritance chain (`Animals -> Pets -> Dog`) and equips `Dog` with a static `bark()` method. |
| `problem3.py` | Implements an `Employee` class using paired `@property` and `@setter` decorators to synchronize salary and percentage increment. |
| `problem4.py` | Implements a `Complex` number class with operator overloading for addition (`__add__`), multiplication (`__mul__`), and display (`__str__`). |
| `problem5.py` | Overloads `+` and `*` operators on a 2D `Vector` class to calculate component-wise addition and products. |
| `problem6.py` | Implements a 3D `Vector(i, j, k)` with string representation (`__str__`), vector addition (`__add__`), and component multiplication (`__mul__`). |
| `problem7.py` | Overloads Python's built-in `len()` function by implementing `__len__()` on a custom vector class wrapping a list. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: Demonstrates subclass extension and constructor delegation using `super().__init__()` to reuse 2D coordinates in a 3D vector.
2. **Problem 2 (`problem2.py`)**: Establishes a clean multilevel inheritance hierarchy (`Dog` inherits from `Pets`, which inherits from `Animals`).
3. **Problem 3 (`problem3.py`)**: Uses paired `@property` and `@setter` to compute dynamic derived attributes and reflect modifications backward to underlying variables.
4. **Problem 4 (`problem4.py`)**: Implements mathematical complex number arithmetic via `__add__` and `__mul__` dunder methods.
5. **Problem 5 (`problem5.py`)**: Overloads operators on 2D vectors, demonstrating how Python translates `v1 + v2` into `v1.__add__(v2)`.
6. **Problem 6 (`problem6.py`)**: Expands vector operator overloading into three dimensions (`i`, `j`, `k`) with custom `__str__` formatting.
7. **Problem 7 (`problem7.py`)**: Implements `__len__()` to allow custom collection classes to respond naturally to Python's built-in `len()` function.

## 🧠 Beginner tip

When implementing mathematical classes like `Complex` or `Vector`, always return a **new instance** of the class from `__add__` and `__mul__` rather than modifying `self` in place. This preserves immutability and allows natural chaining like `a + b + c`.

## 📊 Where this is used in Data Science

Vector math and operator overloading form the core of scientific computing libraries like NumPy and PyTorch. When you add two NumPy arrays (`arr1 + arr2`) or multiply matrices in PyTorch (`tensor1 @ tensor2`), the libraries use dunder methods (`__add__`, `__matmul__`) to execute high-performance low-level kernels behind an intuitive mathematical syntax.

## 🏃 How to Run Each Exercise

Run each exercise script from your terminal:

```bash
python problem1.py
python problem2.py
python problem3.py
python problem4.py
python problem5.py
python problem6.py
python problem7.py
```

## 📖 Related Lessons

- [Chapter 11 - Inheritance and Polymorphism](../chapter_11_inheritance_polymorphism/README.md)

## ⏭️ What's Next

- [Chapter 12 - Exception Handling](../chapter_12_exception_handling/README.md)
