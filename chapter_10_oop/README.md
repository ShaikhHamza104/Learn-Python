# 📚 Topic: Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) structures programs by organizing data (attributes) and behavior (methods) into reusable blueprints called classes. This chapter covers class declaration, class vs. instance attributes, instance methods with `self`, constructors (`__init__`), static utility methods (`@staticmethod`), class-level methods (`@classmethod`), property decorators for getters and setters, encapsulation with protected (`_`) and private (`__`) members, magic/dunder methods (`__len__`, `__str__`, `__repr__`, `__call__`), and introspection using `__dict__` and `help()`.

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_class.py` | Defining a class blueprint with class attributes and creating object instances with custom instance attributes. |
| `02_instance_vs_class_attribute.py` | Attribute resolution hierarchy showing that instance attributes override class attributes of the same name. |
| `03_method.py` | Writing instance methods with `self` and defining utility functions without `self` using `@staticmethod`. |
| `04_constructor.py` | Automatic object initialization upon instantiation using the default `__init__()` constructor method. |
| `05_pass_para_in_cons.py` | Passing parameters directly into `__init__()` to initialize instance attributes dynamically upon object creation. |
| `06_static_method.py` | Combining static greeting methods (`@staticmethod`) with instance attribute modifier methods. |
| `07_class_method.py` | Binding methods to the class itself using `@classmethod` and `cls` to modify class-level attributes across all instances. |
| `08_property.py` | Using the `@property` decorator to convert a method into a read-only attribute getter. |
| `09_setter_and_getter.py` | Building managed attributes with paired `@property` and `@prop.setter` decorators for controlled attribute modification. |
| `10_protected_member.py` | Implementing protected members using the single underscore prefix convention (`_name`) accessible in derived subclasses. |
| `11_private_method.py` | Enforcing strict encapsulation with double underscore private attributes (`__name`), triggering Python name mangling. |
| `12_magic_method.py` | Implementing special dunder methods: `__len__`, `__str__`, `__repr__`, and enabling callable objects with `__call__`. |
| `13_dic_help_method.py` | Object introspection displaying instance attribute dictionaries with `__dict__` and built-in documentation with `help()`. |

## 💡 Key points

1. **Instance vs. Class Attributes**: Class attributes are shared across all instances of a class; instance attributes belong exclusively to a single object and take priority during attribute lookups.
2. **The `self` and `cls` Parameters**: `self` refers to the specific instance invoking a method; `cls` refers to the class object passed automatically into `@classmethod` methods.
3. **Encapsulation Conventions**: A single underscore `_var` indicates protected status by convention; a double underscore `__var` triggers name mangling (`_ClassName__var`) to prevent accidental external access.
4. **Managed Attributes**: Using `@property` and `@setter` provides a clean attribute-like syntax (`obj.name = "val"`) while retaining full validation and computation logic behind the scenes.
5. **Magic / Dunder Methods**: Special methods enclosed in double underscores allow custom classes to integrate with Python's built-in functions (`len(obj)` calls `__len__`, `str(obj)` calls `__str__`, `obj()` calls `__call__`).

## 🧠 Beginner tip

Don't forget `self` as the first parameter of any regular class method! When you invoke `emp.getInfo()`, Python translates that behind the scenes into `Employee.getInfo(emp)`. If your method definition omits `self` and lacks a `@staticmethod` decorator, Python will raise a `TypeError: takes 0 positional arguments but 1 was given`.

## 📊 Where this is used in Data Science

Data science libraries are built on OOP foundations: every scikit-learn estimator (`LinearRegression`, `RandomForestClassifier`) is a class with `.fit()` and `.predict()` methods, while PyTorch models subclass `torch.nn.Module` and implement `forward()` and `__init__()`. Understanding OOP enables data scientists to construct custom transformers, neural network layers, and reproducible ML pipeline classes.

## 🛠️ Code Examples

### Classes, Attributes & Constructors (`01_class.py`, `05_pass_para_in_cons.py`)
```python
class Employee:
    company = "Microsoft"  # Class attribute

    def __init__(self, name, language):
        self.name = name          # Instance attribute
        self.language = language

emp = Employee("Hamza", "Python")
print(emp.name, emp.company)
```

### Class Methods & Static Methods (`06_static_method.py`, `07_class_method.py`)
```python
class Company:
    name = "Microsoft"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name

    @staticmethod
    def greet():
        print("Welcome!")
```

### Properties with Getters & Setters (`09_setter_and_getter.py`)
```python
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split()
```

### Magic Methods (`12_magic_method.py`)
```python
class Worker:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"Worker({self.name})"
```

## 🏋️ Practice Exercises

Sharpen your object-oriented programming skills with the exercises in the practice folder:
- [Chapter 10 Exercises](../chapter_10_oop_exercises/README.md)

## ⏭️ What's Next

- [Chapter 11 - Inheritance and Polymorphism](../chapter_11_inheritance_polymorphism/README.md)
