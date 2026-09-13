# 🐍 Chapter 11 Exercises — Inheritance & Polymorphism Practice 🧬

Welcome to the **Chapter 11 Practice Exercises**! 🚀  
These 7 problems challenge your ability to construct inheritance hierarchies, manage properties with setters, overload arithmetic operators (`+`, `*`), format objects with `__str__`, and hook into `len()` via `__len__`.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 📐 [`problem1.py`](./problem1.py) | 2D to 3D Vector Inheritance | Deriving a 3D vector from a 2D vector class | 🟢 Beginner |
| 🐕 [`problem2.py`](./problem2.py) | Multilevel Pets Hierarchy | `Animals -> Pets -> Dog` multilevel inheritance | 🟢 Beginner |
| 💼 [`problem3.py`](./problem3.py) | Salary Increment Property | Dynamic property calculations with `@prop.setter` | 🟡 Easy-Medium |
| 🔢 [`problem4.py`](./problem4.py) | Complex Numbers Arithmetic | Overloading `+` (`__add__`) and `*` (`__mul__`) | 🟡 Easy-Medium |
| 🧭 [`problem5.py`](./problem5.py) | n-Dimensional Vector Math | Vector addition and dot product overloading | 🔴 Medium |
| 🔤 [`problem6.py`](./problem6.py) | Custom Vector String Representation | Implementing `__str__` (`7i + 8j + 10k`) | 🟢 Beginner |
| 📏 [`problem7.py`](./problem7.py) | Vector Dimensions with `len()` | Overriding `__len__` to return dimension length | 🟢 Beginner |

---

## 📐 Problem 1: 2D & 3D Vectors (`problem1.py`)

### 💻 Code
```python
class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2D Vector: {self.i}i + {self.j}j")

class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"3D Vector: {self.i}i + {self.j}j + {self.k}k")

v2 = Vector2D(1, 2)
v3 = Vector3D(1, 2, 3)
v2.show()
v3.show()
```

▶️ **Run:** `python problem1.py`

---

## 🐕 Problem 2: Pets Hierarchy (`problem2.py`)

### 💻 Code
```python
class Animals:
    animal_type = "Mammal"

class Pets(Animals):
    pet_nature = "Domestic"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")

d = Dog()
print(d.animal_type)  # Mammal
print(d.pet_nature)   # Domestic
d.bark()              # Woof! Woof!
```

▶️ **Run:** `problem2.py`

---

## 💼 Problem 3: Salary Increment with `@property` (`problem3.py`)

### 💻 Code
```python
class Employee:
    salary = 50000
    increment = 20  # 20%

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * (self.increment / 100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary - self.salary) / self.salary) * 100

e = Employee()
print("Salary with default increment:", e.salaryAfterIncrement)  # 60000.0

e.salaryAfterIncrement = 75000
print("New calculated increment %:", e.increment)               # 50.0%
```

▶️ **Run:** `python problem3.py`

---

## 🔢 Problem 4: Complex Number Operations (`problem4.py`)

### 💻 Code
```python
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        real = self.r * other.r - self.i * other.i
        imag = self.r * other.i + self.i * other.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print("Sum:", c1 + c2)       # 4 + 6i
print("Product:", c1 * c2)   # -5 + 10i
```

▶️ **Run:** `python problem4.py`

---

## 🧭 Problems 5, 6 & 7: n-Dimensional Vector Class (`problem5.py` – `problem7.py`)

### 💻 Code
```python
class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __add__(self, other):
        """Vector addition"""
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def __mul__(self, other):
        """Dot product"""
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def __len__(self):
        """Problem 7: Dimensions count"""
        return len(self.coordinates)

    def __str__(self):
        """Problem 6: String representation"""
        components = ["i", "j", "k"]
        terms = [f"{val}{comp}" for val, comp in zip(self.coordinates, components)]
        return " + ".join(terms)

v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

print("Vector representation:", v1)  # 7i + 8j + 10k
print("Dimensions:", len(v1))         # 3
print("Vector Sum:", v1 + v2)         # 8i + 10j + 13k
print("Dot Product:", v1 * v2)        # 7*1 + 8*2 + 10*3 = 53
```

---

## ⏭️ What's Next?
Now learn how to handle unexpected crashes cleanly in **[Chapter 12 — Exception Handling](../chapter_12/README.md)**!
