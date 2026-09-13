"""
📚 Topic: TypedDict

This script demonstrates how to use TypedDict in Python.
TypedDict allows us to describe the expected keys and value types
inside a dictionary.

💡 Key points:
    1️⃣ How to create a normal Python dictionary.
    2️⃣ How to define a TypedDict using a class.
    3️⃣ How to create a dictionary using a TypedDict.
    4️⃣ How to access values from a TypedDict.
    5️⃣ Another way to create a TypedDict using TypedDict().
    6️⃣ How TypedDict helps describe the structure of a dictionary.

🧠 Beginner tip:
    TypedDict does not create a new runtime dictionary type.
    It mainly helps tools such as type checkers understand what
    keys and value types your dictionary should contain.

    Run this file and try changing the value types to see how
    your type checker responds.
"""

from typing import TypedDict


# 📦 Creating a normal dictionary
# A dictionary stores data using key-value pairs.
person_dict = {
    "name": "Ankit",
    "age": 21,
    "city_name": "Mumbai",
}
print(person_dict)


# 🏗️ Creating a TypedDict using a class
# TypedDict allows us to describe the expected structure
# of a dictionary.
class Person(TypedDict):
    name: str
    age: int
    city_name: str
    email: str


# 👤 Creating a Person dictionary
# The variable follows the structure defined by Person.
person_dict1: Person = {
    "name": "Ankit",
    "age": 20,
    "city_name": "Mumbai",
    "email": "ankit@example.com",
}
print(person_dict1)

# 📧 Adding email information
# Because email is defined inside Person, we can include it
# as part of the dictionary.
person_dict2: Person = {
    "name": "Ankit",
    "age": 22,
    "city_name": "Mumbai",
    "email": "hamza@example.com",
}
print(person_dict2)

# 📝 Creating another Person dictionary
# A TypedDict can also be created by calling Person().
person_dict3 = Person(
    name="Hamza",
    age=30,
    city_name="Kurla",
    email="kmohdhamza09@gmail.com",
)

# 🔍 Accessing a value
# The get() method returns the value associated with the key.
print(person_dict3.get("name"))

# 🐾 Creating another TypedDict
# TypedDict can also be created using the functional syntax.
Animal = TypedDict(
    "Animal",
    {
        "name": str,
        "sound": str,
        "age": int,
    },
)

# 🐶 Creating an Animal dictionary
# The dictionary follows the structure defined by Animal.
animal = Animal(
    name="Dog",
    sound="Woof",
    age=5,
)
print(animal)

# 🐕 Creating another Animal dictionary
animal_dict: Animal = {
    "name": "Tuffy",
    "sound": "bark",
    "age": 3,
}
print(animal_dict)
