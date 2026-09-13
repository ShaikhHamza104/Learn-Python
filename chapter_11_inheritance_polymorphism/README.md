# 📚 Topic: Inheritance and Polymorphism

Inheritance and polymorphism are core object-oriented programming principles that foster code reuse, interface uniformity, and modular design. This chapter covers single inheritance, multiple inheritance, multilevel inheritance chains, constructor delegation with `super()`, method overloading patterns, method overriding, abstract base classes using Python's `abc` module, polymorphic interfaces, arithmetic operator overloading via magic methods, and composition ("has-a") vs. inheritance ("is-a").

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_intro_to_inheritance.py` | Basic inheritance syntax where child class `B(A)` inherits methods from parent class `A`. |
| `02_single_inheritance.py` | Single inheritance hierarchy demonstrating attribute inheritance and overriding parent class attributes. |
| `03_multiple_inheritance.py` | Multiple inheritance (`class Theory(Ptt1, Ptt2, Microproject)`) combining methods and data from three distinct parent classes. |
| `04_multiple_level_inheritance.py` | Multilevel inheritance chain (`A -> B -> C`) enabling child class `C` to access attributes from all ancestors. |
| `05_super_method.py` | Delegating initialization to the parent class constructor using `super().__init__()`. |
| `06_method_overloading.py` | Simulating method overloading in Python using optional default parameters (`a=None, b=None, c=None`). |
| `07_method_overriding.py` | Overriding parent class methods in child classes to customize specialized behavior (`Dog.say()` overrides `Animal.say()`). |
| `08_abstract_class.py` | Enforcing required interface methods in subclasses using `abc.ABC` and the `@abstractmethod` decorator. |
| `09_polymorphism.py` | Polymorphism across independent classes (`India`, `USA`) sharing identical method signatures invoked via a unified loop. |
| `10_operator_overloading.py` | Overloading arithmetic operators (`+`, `-`, `*`, `/`) for custom objects using `__add__`, `__sub__`, `__mul__`, and `__truediv__`. |
| `11_composition.py` | Demonstrating the composition design pattern ("has-a" relationship) by embedding an `Employee` object inside a `Bonus` class. |

## 💡 Key points

1. **Inheritance for Code Reuse**: Subclasses automatically gain access to all methods and attributes defined in parent classes without rewriting logic.
2. **The `super()` Method**: Allows child classes to cleanly invoke parent implementations (especially `super().__init__()`), preventing redundant initialization.
3. **Abstract Base Classes**: Subclasses of an `ABC` with `@abstractmethod` cannot be instantiated unless they implement every abstract method.
4. **Method Overloading vs. Overriding**: Python does not support native method signature overloading; instead, use default arguments or `*args`. Method overriding occurs when a child class redefines a parent method with the same name.
5. **Composition over Inheritance**: Composition ("has-a") embeds instances of other classes as attributes, offering looser coupling and greater flexibility than rigid inheritance ("is-a") trees.

## 🧠 Beginner tip

Remember that Python does not support multiple methods with the same name and different parameters (traditional method overloading)! If you write `def sum(self, a, b): ...` and then write `def sum(self, a, b, c): ...` below it, the second definition simply overwrites the first. Use default arguments (`c=None`) or `*args` to handle variable argument signatures.

## 📊 Where this is used in Data Science

Inheritance and polymorphism are the architectural backbone of data science frameworks. In scikit-learn, all estimators inherit from `BaseEstimator` and implement polymorphic `.fit()` and `.predict()` methods. In deep learning (PyTorch), every custom neural network inherits from `torch.nn.Module`, leveraging `super().__init__()` to register layers and overriding `forward()` to define the computation graph.

## 🛠️ Code Examples

### Super() and Single Inheritance (`05_super_method.py`)
```python
class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a, b)
        print(f"Sum: {self.a + self.b}")
```

### Abstract Base Classes (`08_abstract_class.py`)
```python
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def side(self):
        pass

class Triangle(Polygon):
    def side(self):
        print("I have 3 sides")
```

### Operator Overloading (`10_operator_overloading.py`)
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1, v2 = Vector(2, 3), Vector(4, 5)
print(v1 + v2)  # (6, 8)
```

### Composition (`11_composition.py`)
```python
class Bonus:
    def __init__(self):
        self.employee = Employee()  # "Has-a" relationship
```

## 🏋️ Practice Exercises

Sharpen your OOP and inheritance skills with the exercises in the practice folder:
- [Chapter 11 Exercises](../chapter_11_inheritance_polymorphism_exercises/README.md)

## ⏭️ What's Next

- [Chapter 12 - Exception Handling](../chapter_12_exception_handling/README.md)
