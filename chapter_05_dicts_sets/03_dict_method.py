"""
📚 Topic: Dictionary Methods

This script explores commonly used dictionary methods for inspecting and
manipulating key-value collections.

💡 Key points:
    1️⃣ Extracting views: `keys()`, `values()`, and `items()`
    2️⃣ Safe lookups using `dict.get(key, default)`
    3️⃣ Merging dictionaries using `dict.update()`

🧠 Beginner tip:
    Views returned by `.keys()` and `.items()` are dynamic and reflect future
    changes made to the underlying dictionary.
"""
# 📚 Dictionary of marks
# Student names are the keys and their marks are the values.
mark = {"Rohan": 70, "Harry": 100, "Sonali": 80, "Mari": 75, "Yusuf": 95}


# 🔑 Get all keys from the dictionary
# keys() returns all the keys present in the dictionary.
print(mark.keys())

# Output:
# dict_keys(['Rohan', 'Harry', 'Sonali', 'Mari', 'Yusuf'])


# 💯 Get all values from the dictionary
# values() returns all the values stored in the dictionary.
print(mark.values())

# Output:
# dict_values([70, 100, 80, 75, 95])


# 🔗 Get all key-value pairs
# items() returns each key and its corresponding value together.
print(mark.items())

# Output:
# dict_items([
#     ('Rohan', 70),
#     ('Harry', 100),
#     ('Sonali', 80),
#     ('Mari', 75),
#     ('Yusuf', 95)
# ])


# 🔍 Get a value using its key
# get() returns the value associated with the given key.
#
# Here, we are asking for Yusuf's marks.
print(mark.get("Yusuf"))

# Output:
# 95


# 🔄 Update the dictionary
# update() can be used to add new key-value pairs
# or change the value of an existing key.
#
# Here:
# • Yusuf's marks are changed from 95 to 99.
# • A new student "Renuka" is added with 95 marks.
mark.update({"Yusuf": 99, "Renuka": 95})

print(mark)

# Output:
# {'Rohan': 70, 'Harry': 100, 'Sonali': 80,
#  'Mari': 75, 'Yusuf': 99, 'Renuka': 95}


# 🗑️ Remove an item using pop()
# pop() removes the specified key and returns its value.
#
# This line is commented out, so it will not run.
# If we uncomment it, "Rohan" will be removed
# and the output will be 70.
#
# print(mark.pop("Rohan"))


# 🧹 Remove the last inserted key-value pair
# popitem() removes and returns the last inserted pair.
#
# At this point, "Renuka" was the last item added,
# so it will be removed.
print(mark.popitem())

# Output:
# ('Renuka', 95)


# 📋 Make a copy of the dictionary
# copy() creates a new dictionary containing the same data.
#
# This is useful when we want another dictionary
# without directly assigning the same dictionary.
my_mark = mark.copy()

print(my_mark)

# Output:
# {'Rohan': 70, 'Harry': 100, 'Sonali': 80,
#  'Mari': 75, 'Yusuf': 99}


# 🧹 Remove all items from the copied dictionary
# clear() removes everything from the dictionary.
my_mark.clear()

print(my_mark)

# Output:
# {}


# ❌ Delete the dictionary completely
# del removes the dictionary variable itself.
#
# After this line, we cannot use `my_mark` again
# unless we create it again.
del my_mark


# ➕ Add a key only if it does not already exist
# setdefault() checks whether the key is already present.
#
# If "Mukesh" does not exist, it adds the key
# with the given default value of 70.
#
# If "Mukesh" already existed, its existing value
# would not be changed.
mark.setdefault("Mukesh", 70)

print(mark)

# Output:
# {'Rohan': 70, 'Harry': 100, 'Sonali': 80,
#  'Mari': 75, 'Yusuf': 99, 'Mukesh': 70}
