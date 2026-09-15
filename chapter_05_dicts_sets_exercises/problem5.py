"""
📚 Topic: Chapter 05 Exercise - Problem 5

Identify the type of an empty set representation `s = {}`.

💡 Key points:
    1️⃣ `{}` is reserved for initializing empty dictionaries
    2️⃣ `type({})` evaluates to `<class 'dict'>`
    3️⃣ Initializing an empty set requires `set()`
"""
# 📚 Create an empty dictionary
# Empty curly braces `{}` represent a dictionary in Python.
s = {}


# 🔍 Check the type of `s`
print(type(s))

# Output:
# <class 'dict'>


# 💡 To create an empty set, we would write:
#
# s = set()
#
# print(type(s))
#
# Output:
# <class 'set'>
