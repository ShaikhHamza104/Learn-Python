"""
📚 Topic: Python Lists

This script introduces lists as ordered, mutable sequences capable of storing
heterogeneous elements.

💡 Key points:
    1️⃣ Creating lists using square brackets `[]`
    2️⃣ Accessing elements via zero-based indexing and slicing
    3️⃣ Mutability: modifying list elements directly in-place

🧠 Beginner tip:
    Unlike strings, lists can be altered after creation without creating a
    new object in memory.
"""
# ============================================================
# 🎯 WHAT IS A LIST?
# ============================================================
# A list is a collection of items stored in a single variable.
# Lists are MUTABLE = you can change them after creation! 🔄
# Lists can hold ANY data type: numbers, strings, booleans, etc.
# ============================================================


# ============================================================
# 1️⃣ WAY 1: Using Square Brackets [ ] (Most Common!) ⭐
# ============================================================

li = [1, 2, 3, 4, True, 3.14, None, "Hamza"]

print("Way 1 (Square Brackets):", li)
# Output: [1, 2, 3, 4, True, 3.14, None, 'Hamza']


# ============================================================
# 2️⃣ WAY 2: Using list() Constructor
# ============================================================
# ⚠️ list() takes ONLY 1 argument - you must pass items inside [ ] or ( )
# ❌ list(1, 2, 3)     ← WRONG! Too many arguments
# ✅ list([1, 2, 3])   ← CORRECT! One list argument
# ✅ list((1, 2, 3))   ← CORRECT! One tuple argument
# ============================================================

li2 = list([1, 2, 3, 4, True, 3.14, None, "Hamza"])

print("Way 2 (list() constructor):", li2)
# Output: [1, 2, 3, 4, True, 3.14, None, 'Hamza']


# ============================================================
# 🧪 LET'S VERIFY BOTH ARE THE SAME!
# ============================================================

print("\n--- Comparison ---")
print("li  == li2 ?", li == li2)  # True ✅
print("Type of li:", type(li))  # <class 'list'>


# ============================================================
# 💡 QUICK TIP: Creating an Empty List
# ============================================================

empty1 = []  # Way 1: Square brackets (Recommended!)
empty2 = list()  # Way 2: list() constructor

print("\nEmpty list 1:", empty1)
print("Empty list 2:", empty2)


# ============================================================
# 🎉 SUMMARY
# ============================================================
# ✅ Use [ ] for creating lists (simple & fast!)
# ✅ Use list() when converting other types to list
# ✅ list() takes ONLY 1 argument (an iterable)
# ============================================================
