"""
📚 Topic: Tuple

This script demonstrates tuple using exception handling.

💡 Key points:
    1️⃣ the basic syntax for tuple
    2️⃣ how exception handling fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    tuple affects the result.
"""


# ============================================================
# 🎯 WHAT IS A TUPLE?
# ============================================================
# Tuple = A collection of items that CANNOT be changed after creation
# Think of it as a "read-only" list 📖
# Use tuples when you want data to stay safe and unchanged!
# ============================================================


# ============================================================
# 1️⃣ CREATING AN EMPTY TUPLE
# ============================================================

t = ()
print("📦 Empty Tuple:", t)
print("Type:", type(t))  # <class 'tuple'>
print()


# ============================================================
# 2️⃣ CREATING A SINGLE-ELEMENT TUPLE ⚠️
# ============================================================
# VERY IMPORTANT: You MUST add a comma after the single item!
# Without the comma, Python thinks it's just a number in brackets!

# ✅ CORRECT way:
t = (1,)
print("✅ Single-element tuple:", t)
print("Type:", type(t))  # <class 'tuple'>

# ❌ WRONG way (DON'T DO THIS!):
t_wrong = 1
print("❌ Without comma:", t_wrong)
print("Type:", type(t_wrong))  # <class 'int'> ← NOT a tuple!
print()


# ============================================================
# 3️⃣ CREATING A MULTI-ELEMENT TUPLE
# ============================================================

t = (1, 2, 3, 4, 5, 6, 7)
print("📋 Multi-element tuple:", t)
print("Type:", type(t))  # <class 'tuple'>
print()


# ============================================================
# 4️⃣ ACCESSING TUPLE ELEMENTS (Same as lists!)
# ============================================================

print("🔍 Accessing Elements:")
print("t[0]  =", t[0])  # First element
print("t[3]  =", t[3])  # 4th element
print("t[-1] =", t[-1])  # Last element
print()


# ============================================================
# 5️⃣ WHY USE TUPLES? 🤔
# ============================================================

print("💡 Why Tuples?")
print("✅ Faster than lists (better performance)")
print("✅ Protects data from accidental changes")
print("✅ Can be used as dictionary keys (lists cannot!)")
print("✅ Good for fixed data like coordinates, days, etc.")
print()


# ============================================================
# 6️⃣ TRYING TO CHANGE A TUPLE (Will Give ERROR!) ❌
# ============================================================

print("🚫 Tuples are IMMUTABLE:")
try:
    t[0] = 100  # This will FAIL!
except TypeError as e:
    print("Error:", e)
print()


# ============================================================
# 🎯 QUICK REFERENCE CHEAT SHEET
# ============================================================

print("=" * 50)
print("📌 TUPLE CHEAT SHEET")
print("=" * 50)

cheat_sheet = """
┌────────────────────────┬──────────────────────────────┐
│ Syntax                 │ Result                       │
├────────────────────────┼──────────────────────────────┤
│ ()                     │ Empty tuple                  │
│ (1,)                   │ Single-element tuple ✅      │
│ (1)                    │ Just integer 1 ❌            │
│ (1, 2, 3)              │ Multi-element tuple          │
│ 1, 2, 3                │ Also a tuple (no brackets!)  │
│ t[0]                   │ Access first element         │
│ t[-1]                  │ Access last element          │
│ len(t)                 │ Get number of elements       │
│ t.count(x)             │ Count occurrences of x       │
│ t.index(x)             │ Find index of x              │
└────────────────────────┴──────────────────────────────┘

⚠️ REMEMBER: The comma (,) makes it a tuple, not the brackets!
"""
print(cheat_sheet)

print("🎉 Tuples = Lists that you promise not to change! 🔒")
