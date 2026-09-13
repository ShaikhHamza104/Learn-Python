# 🐍 Chapter 11 — Inheritance & Polymorphism: Advanced OOP 🧬

Welcome to Chapter 11! Building on basic OOP concepts, this chapter explores **Inheritance** (enabling code reuse by deriving child classes from parent classes), **Polymorphism** (allowing different classes to be treated through a uniform interface), **Abstract Base Classes**, **Operator Overloading**, and **Composition**.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_intro_to_inheritance.py` | What is Inheritance? | Extending base classes with `class Child(Parent):` |
| 02 | `02_single_inheritance.py` | Single Inheritance | One parent class to one child class |
| 03 | `03_multiple_inheritance.py` | Multiple Inheritance | Inheriting from multiple parent classes `class C(A, B):` |
| 04 | `04_multiple_level_inheritance.py` | Multilevel Inheritance | Chain inheritance `Grandparent -> Parent -> Child` |
| 05 | `05_super_method.py` | The `super()` Function | Calling parent constructors and methods |
| 06 | `06_method_overloading.py` | Method Overloading Patterns | Default arguments and `*args` for flexible signatures |
| 07 | `07_method_overriding.py` | Method Overriding | Replacing parent implementations in child classes |
| 08 | `08_abstract_class.py` | Abstract Base Classes (`abc`) | Enforcing interfaces using `@abstractmethod` |
| 09 | `09_polymorphism.py` | Polymorphism & Duck Typing | Common interface across different class types |
| 10 | `10_operator_overloading.py` | Operator Overloading | Implementing `__add__`, `__mul__`, `__eq__` |
| 11 | `11_composition.py` | Composition vs. Inheritance | "Has-a" relationship vs. "Is-a" relationship |

---

## 🧬 1. Inheritance Hierarchy & `super()` (`02_single_inheritance.py` – `05_super_method.py`)

```python
class Animal:
    def __init__(self, species: str):
        self.species = species

    def breathe(self):
        print("Breathing air...")

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        # Call the parent constructor
        super().__init__(species="Canine")
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

dog = Dog("Buddy", "Golden Retriever")
dog.breathe()  # Inherited from Animal
dog.bark()     # Defined on Dog
```

---

## 🎭 2. Polymorphism & Method Overriding (`07_method_overriding.py`, `09_polymorphism.py`)

Different classes can define the same method name, allowing uniform treatment:

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print("Area:", s.area())  # Polymorphic execution!
```

---

## 🚫 3. Abstract Base Classes (`08_abstract_class.py`)

Abstract classes cannot be instantiated directly; they enforce that subclasses implement required methods:

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class UPI(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Paid ₹{amount} via UPI.")
        return True
```

---

## ➕ 4. Operator Overloading (`10_operator_overloading.py`)

Teach Python operators (`+`, `*`, `==`, `<`) how to work with your custom classes:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        """Overloads the + operator"""
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 7)
print(p1 + p2)  # Point(6, 10)
```

---

## 🏋️ Practice Exercises
Test vectors, pets hierarchy, property setters, and complex number arithmetic in **[chapter_11_exercises/](../chapter_11_exercises/README.md)**!

---

## ⏭️ What's Next?
Now learn how to protect your code from crashes in **[Chapter 12 — Exception Handling](../chapter_12/README.md)**!
