# 🐍 Chapter 10 — Object-Oriented Programming (OOP) 🏗️

Welcome to Chapter 10! **Object-Oriented Programming (OOP)** is one of the most widely used paradigms in software development. OOP models real-world entities into programs by bundling **state (data/attributes)** and **behavior (methods/functions)** together into **Classes** and **Objects**.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_class.py` | Classes and Objects | Defining blueprints and instantiating objects |
| 02 | `02_instance_vs_class_attribute.py` | Attributes Scope | Class variables vs. instance variables |
| 03 | `03_method.py` | Methods | Instance methods with `self` parameter |
| 04 | `04_constructor.py` | Constructors (`__init__`) | Initializing objects automatically upon creation |
| 05 | `05_pass_para_in_cons.py` | Parameterized Constructors | Passing arguments when instantiating classes |
| 06 | `06_static_method.py` | `@staticmethod` | Utility methods that don't need `self` or `cls` |
| 07 | `07_class_method.py` | `@classmethod` | Methods bound to the class (`cls`) rather than instance |
| 08 | `08_property.py` | `@property` Decorator | Defining getter methods accessed like attributes |
| 09 | `09_setter_and_getter.py` | Getters & Setters | Validating attribute updates with `@prop.setter` |
| 10 | `10_protected_member.py` | Protected Attributes | Convention with single underscore `_var` |
| 11 | `11_private_method.py` | Private Attributes | Name mangling with double underscore `__var` |
| 12 | `12_magic_method.py` | Dunder / Magic Methods | Operator overloading with `__str__`, `__len__`, `__add__` |
| 13 | `13_dic_help_method.py` | Object Introspection | Inspecting objects with `__dict__` and `help()` |

---

## 🏛️ 1. Classes, Objects, and Constructors (`01_class.py`, `04_constructor.py`)

A **Class** is a blueprint, and an **Object** is an instance created from that blueprint.

```python
class Employee:
    # Class attribute (shared by all instances)
    company = "Microsoft"

    # Constructor method: runs when Employee() is called
    def __init__(self, name: str, salary: int):
        # Instance attributes (unique to each object)
        self.name = name
        self.salary = salary

    # Instance method
    def get_info(self):
        return f"{self.name} earns ₹{self.salary} at {self.company}."

emp1 = Employee("Hamza", 120000)
print(emp1.get_info())
```

---

## ⚡ 2. Static and Class Methods (`06_static_method.py`, `07_class_method.py`)

```python
class MathUtils:
    factor = 10

    # Static method: behaves like a normal function within class namespace
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: receives 'cls' instead of 'self'
    @classmethod
    def update_factor(cls, new_factor):
        cls.factor = new_factor
```

---

## 🔒 3. Encapsulation & Properties (`08_property.py` – `11_private_method.py`)

```python
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._protected_id = "ACC_123"  # Protected (convention)
        self.__balance = balance        # Private (name mangled)

    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount: float):
        """Setter with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount
```

---

## ✨ 4. Magic / Dunder Methods (`12_magic_method.py`)

Dunder (Double Underscore) methods allow your custom objects to hook into Python's built-in behaviors:

```python
class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    def __len__(self):
        return self.pages

book = Book("Fluent Python", 800)
print(book)       # Calls __str__ -> 'Fluent Python' (800 pages)
print(len(book))  # Calls __len__ -> 800
```

---

## 🏋️ Practice Exercises
Apply your OOP knowledge with 4 practical design exercises in **[chapter_10_exercises/](../chapter_10_exercises/README.md)**!

---

## ⏭️ What's Next?
Take OOP to the next level with code reuse in **[Chapter 11 — Inheritance](../chapter_11/README.md)**!
