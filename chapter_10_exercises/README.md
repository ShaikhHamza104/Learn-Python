# 🐍 Chapter 10 Exercises — Object-Oriented Programming Practice 🏗️

Welcome to the **Chapter 10 Practice Exercises**! 🚀  
These 4 exercises focus on designing Python classes, managing instance vs. class attributes, adding mathematical capabilities, and modeling real-world domain services (like a Railway ticket reservation system).

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 💻 [`problem1.py`](./problem1.py) | Microsoft Programmer Registry | Initializing instance data with class company attribute | 🟢 Beginner |
| 🧮 [`problem2.py`](./problem2.py) | Scientific Calculator Class | Methods calculating square, cube, and square root | 🟢 Beginner |
| ⚖️ [`problem3.py`](./problem3.py) | Class vs. Instance Attributes | Proving attribute resolution order and shadowing | 🟡 Easy-Medium |
| 🚆 [`problem4.py`](./problem4.py) | Railway Reservation System | State-tracking class with booking, fare, and status | 🟡 Easy-Medium |

---

## 💻 Problem 1: Programmer Class (`problem1.py`)

### ❓ Objective
Create a class `Programmer` for storing information of programmers working at Microsoft.

### 💻 Code
```python
class Programmer:
    company = "Microsoft"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def get_details(self):
        print(f"Company: {self.company} | Name: {self.name} | Dept: {self.department} | Salary: ₹{self.salary}")

p1 = Programmer("Hamza", "Azure Cloud", 150000)
p2 = Programmer("Ali", "Windows Core", 130000)

p1.get_details()
p2.get_details()
```

▶️ **Run:** `python problem1.py`

---

## 🧮 Problem 2: Calculator Class (`problem2.py`)

### ❓ Objective
Write a class `Calculator` capable of finding the square, cube, and square root of a number.

### 💻 Code
```python
import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

calc = Calculator(9)
print("Square:", calc.square())       # 81
print("Cube:", calc.cube())           # 729
print("Square Root:", calc.square_root()) # 3.0
```

▶️ **Run:** `python problem2.py`

---

## ⚖️ Problem 3: Attribute Shadowing Verification (`problem3.py`)

### ❓ Objective
Create a class with a class attribute `a`; create an object from it and set `a` directly using `object.a = 0`. Does this change the class attribute?

### 💻 Code
```python
class Demo:
    a = 4  # Class attribute

obj = Demo()
print("Initial object attribute:", obj.a)  # 4 (falls back to class attribute)

obj.a = 0  # Creates an INSTANCE attribute on obj
print("Updated object attribute:", obj.a)  # 0
print("Class attribute:", Demo.a)         # 4 (Unchanged!)
```

### 💡 Key Takeaway
- Setting `obj.a = 0` creates a new instance variable on `obj`.
- It does **not** change the class attribute `Demo.a`.

▶️ **Run:** `python problem3.py`

---

## 🚆 Problem 4: Railway Reservation System (`problem4.py`)

### ❓ Objective
Write a class `Train` which has methods to book a ticket, get seat status, and get fare information.

### 💻 Code
```python
class Train:
    def __init__(self, name, fare, total_seats):
        self.name = name
        self.fare = fare
        self.seats = total_seats

    def get_status(self):
        print(f"Train: {self.name} | Available Seats: {self.seats}")

    def get_fare_info(self):
        print(f"Fare per ticket on {self.name}: ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print(f"✅ Ticket booked successfully on {self.name}!")
            self.seats -= 1
        else:
            print(f"❌ Sorry, {self.name} is fully booked!")

rajdhani = Train("Rajdhani Express", 2500, 2)
rajdhani.get_status()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.book_ticket()  # Rejected
rajdhani.get_status()
```

▶️ **Run:** `python problem4.py`

---

## ⏭️ What's Next?
Next, discover how to inherit and extend behaviors across classes in **[Chapter 11 — Inheritance](../chapter_11/README.md)**!
