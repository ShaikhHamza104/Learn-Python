"""
📚 Topic: Namespace and Scope (LEGB Rule)

This script demonstrates what a namespace is, the 4 types of scope in
Python, and the LEGB rule Python uses to look up a variable's name.

💡 Key points:
    1️⃣ the basic syntax for global and nonlocal keywords
    2️⃣ how the LEGB rule (Local, Enclosing, Global, Built-in) fits in
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    namespace and scope affects the result.
"""

# ---------------------------------------------------
# What is a namespace?
# ---------------------------------------------------
# A namespace is a space that holds names (identifiers). Think of it
# as a dictionary of names (keys) mapped to the actual objects (values).
#
# There are 4 types of namespaces in Python:
#   1. Built-in Namespace   - things like print(), len(), str
#   2. Global Namespace     - variables defined at the top of a file
#   3. Enclosing Namespace  - variables in an outer function
#   4. Local Namespace      - variables inside the current function

# ---------------------------------------------------
# What is scope? The LEGB rule
# ---------------------------------------------------
# A scope is the region of code where a namespace can be directly
# accessed. When Python looks for a name, it searches in this order:
#   Local -> Enclosing -> Global -> Built-in
# If it's not found anywhere, Python raises a NameError.

# ---------------------------------------------------
# 1. Local and Global - different variables
# ---------------------------------------------------
a = 2  # global variable


def temp():
    b = 3  # local variable, only exists inside temp()
    print(b)


temp()
print(a)


# ---------------------------------------------------
# 2. Local shadows Global when they share the same name
# ---------------------------------------------------
a = 2


def temp():
    a = 3  # this creates a NEW local 'a', separate from global
    print(a)  # prints the LOCAL a (3)


temp()
print(a)  # global 'a' is untouched, still 2


# ---------------------------------------------------
# 3. If local doesn't have it, Python looks in global (LEGB in action)
# ---------------------------------------------------
a = 2


def temp():
    print(a)  # no local 'a' found, so Python checks global -> 2


temp()
print(a)


# ---------------------------------------------------
# 4. You CANNOT edit a global variable directly from inside a function
# ---------------------------------------------------
# This line would raise: UnboundLocalError: local variable 'a'
# referenced before assignment
#
# a = 2
# def temp():
#     a += 1          # Python sees 'a =' and assumes 'a' is LOCAL,
#     print(a)         # but it hasn't been created yet locally!
# temp()


# ---------------------------------------------------
# 5. The 'global' keyword - editing a global variable on purpose
# ---------------------------------------------------
a = 2


def temp():
    global a  # tells Python: "use the GLOBAL a, not a local one"
    a += 1
    print(a)


temp()
print(a)  # global 'a' really changed this time, now 3


# ---------------------------------------------------
# 6. Function parameters are always local
# ---------------------------------------------------
def temp(z):
    print(z)


a = 5
temp(5)
print(a)
# print(z)   would raise NameError - z only exists inside temp()


# ---------------------------------------------------
# 7. Built-in scope - things Python already knows without importing
# ---------------------------------------------------
import builtins

print(len(dir(builtins)))  # a big list of built-in names Python provides


# ---------------------------------------------------
# ⚠️ Common mistake: accidentally overwriting a built-in
# ---------------------------------------------------
# L = [1, 2, 3]
# print(max(L))         # works fine, uses the built-in max()
#
# def max():
#     print("hello")
#
# print(max(L))          # TypeError! your own max() replaced the
#                         # built-in one, and it takes 0 arguments


# ---------------------------------------------------
# 8. Enclosing scope - a function inside another function
# ---------------------------------------------------
def outer():
    a = 1

    def inner():
        print(a)  # inner() can READ outer()'s variable

    inner()
    print("outer function")


outer()
print("main program")


# ---------------------------------------------------
# 9. The 'nonlocal' keyword - editing an enclosing variable on purpose
# ---------------------------------------------------
def outer():
    a = 1

    def inner():
        nonlocal a  # tells Python: use outer()'s 'a', not a new one
        a += 1
        print("inner", a)

    inner()
    print("outer", a)


outer()
print("main program")


# ---------------------------------------------------
# 🆚 global vs nonlocal
# ---------------------------------------------------
# global    -> lets a function edit a variable from the GLOBAL scope
# nonlocal  -> lets a nested function edit a variable from the
#              ENCLOSING (outer function's) scope, not global
