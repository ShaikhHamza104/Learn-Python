"""
📚 Topic: Opration List

This script demonstrates opration list using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for opration list
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    opration list affects the result.
"""


# ============================================================
# 1️⃣ CREATE a List (C in CRUD)
# ============================================================
# Lists can hold ANY data type together!
# Numbers, booleans, floats, None, strings - all in one place! 🎒

l = [1, 2, 3, 4, True, 3.14, None, "Hamza"]  # noqa: E741

print("📝 Original List:")
print(l)
# Output: [1, 2, 3, 4, True, 3.14, None, 'Hamza']


# ============================================================
# 2️⃣ READ / ACCESS Values (R in CRUD) 🔍
# ============================================================
# Python uses INDEXING to access items
# Index starts from 0 (NOT 1!) 🎯

print("\n🔍 Accessing Values:")

# Index:  0   1   2   3    4      5      6        7
# Value: [1,  2,  3,  4, True, 3.14, None, "Hamza"]

print("l[0]  =", l[0])  # First item  → 1
print("l[4]  =", l[4])  # 5th item    → True
print("l[-1] =", l[-1])  # Last item   → "Hamza" (negative index!)
print("l[-2] =", l[-2])  # 2nd last    → None


# ============================================================
# 3️⃣ UPDATE a List (U in CRUD) ✏️
# ============================================================
# Lists are MUTABLE = you can change values after creation! 🔄

print("\n✏️ Updating Values:")

# Change first item (index 0)
l[0] = 0
print("After l[0] = 0  :", l)

# Change last item using negative index
l[-1] = "Rohan"
print("After l[-1] = 'Rohan':", l)


# ============================================================
# 4️⃣ DELETE Values (D in CRUD) 🗑️
# ============================================================
# Use 'del' keyword to remove items by index

print("\n🗑️ Deleting Values:")

# Delete item at index 2 (which is 3)
del l[2]
print("After del l[2]  :", l)

# Delete last item
del l[-1]
print("After del l[-1] :", l)


# ============================================================
# 🎯 QUICK REFERENCE CHEAT SHEET
# ============================================================

print("\n📌 Quick Reference:")
print("┌─────────────────┬────────────────────────────┐")
print("│ Operation       │ Syntax                     │")
print("├─────────────────┼────────────────────────────┤")
print("│ Create          │ l = [1, 2, 3]              │")  # noqa: E741
print("│ Read (index)    │ l[0]                       │")
print("│ Read (last)     │ l[-1]                      │")
print("│ Update          │ l[0] = 100                 │")
print("│ Delete (index)  │ del l[0]                   │")
print("└─────────────────┴────────────────────────────┘")

print("\n🎉 Remember: Index starts at 0, not 1!")
