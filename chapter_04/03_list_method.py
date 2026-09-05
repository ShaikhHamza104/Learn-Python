"""
📚 Topic: List Method

This script demonstrates list method using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for list method
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    list method affects the result.
"""


# ============================================================
# 1️⃣ CREATE & INITIALIZE
# ============================================================

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # noqa: E741

print("📝 Original List:", l)


# ============================================================
# 2️⃣ GET LIST INFO
# ============================================================

print("\n📏 List Info:")
print("Length of list:", len(l))  # Counts total items
print("Count of 2:", l.count(2))  # Counts occurrences of a value
print("Index of 5:", l.index(5))  # Finds position of a value


# ============================================================
# 3️⃣ ADD ELEMENTS (3 Ways!)
# ============================================================

print("\n➕ Adding Elements:")

# append() → Add ONE item at the END
l.append(10)
print("After append(10)     :", l)

# insert() → Add item at SPECIFIC position
l.insert(0, 0)  # insert(index, value)
print("After insert(0, 0)   :", l)

# extend() → Add MULTIPLE items at the END
l.extend([11, 12, 13, 14, 15])
print("After extend([11-15]):", l)


# ============================================================
# 4️⃣ REMOVE ELEMENTS (3 Ways!)
# ============================================================

print("\n➖ Removing Elements:")

# remove() → Delete by VALUE (first match only)
l.remove(0)
print("After remove(0)      :", l)

# pop() → Delete by INDEX & return the value
popped = l.pop(9)  # Removes item at index 9
print("Popped value:", popped)
print("After pop(9)         :", l)

# del → Delete by INDEX (no return value)
del l[0]
print("After del l[0]       :", l)


# ============================================================
# 5️⃣ SORT & REVERSE
# ============================================================

print("\n🔀 Sorting & Reversing:")

# sort() → Sort in ascending/descending order
l.sort(reverse=True)  # Descending order
print("After sort(reverse=True):", l)

# reverse() → Flip the list (mirror image)
l.reverse()
print("After reverse()         :", l)


# ============================================================
# 6️⃣ COPY & CLEAR
# ============================================================

print("\n📋 Copy & Clear:")

# copy() → Create a separate copy (not linked to original!)
l2 = l.copy()
print("l2 (copy of l)   :", l2)

# clear() → Empty the list (remove all items)
l2.clear()
print("l2 after clear() :", l2)
print("l (unchanged)    :", l)


# ============================================================
# 🎯 QUICK REFERENCE CHEAT SHEET
# ============================================================

print("\n" + "=" * 50)
print("📌 LIST METHODS CHEAT SHEET")
print("=" * 50)

cheat_sheet = """
┌─────────────────┬──────────────────────────────┬─────────────────────────────┐
│ Method          │ What It Does                 │ Example
│
├─────────────────┼──────────────────────────────┼─────────────────────────────┤
│ len(l)          │ Get total items              │ len([1,2,3]) → 3
│
│ l.append(x)     │ Add x at END                 │ [1,2].append(3) → [1,2,3]
│
│ l.insert(i,x)   │ Add x at index i             │ [1,3].insert(1,2) → [1,2,3]
│
│ l.extend([...]) │ Add multiple at END          │ [1,2].extend([3,4])
│
│ l.remove(x)     │ Remove FIRST x by value      │ [1,2,2].remove(2) → [1,2]
│
│ l.pop(i)        │ Remove at index i & return   │ [1,2,3].pop(1) → returns 2
│
│ del l[i]        │ Remove at index i            │ del [1,2,3][0] → [2,3]
│
│ l.sort()        │ Sort ascending               │ [3,1,2].sort() → [1,2,3]
│
│ l.sort(reverse) │ Sort descending              │ [1,2,3].sort(True) →
[3,2,1]│
│ l.reverse()     │ Flip the list                │ [1,2,3].reverse() → [3,2,1]
│
│ l.count(x)      │ Count occurrences of x       │ [1,2,2].count(2) → 2
│
│ l.index(x)      │ Find position of x           │ [1,2,3].index(2) → 1
│
│ l.copy()        │ Create a new copy            │ l2 = l.copy()
│
│ l.clear()       │ Empty the list               │ [1,2,3].clear() → []
│
└─────────────────┴──────────────────────────────┴─────────────────────────────┘
"""
print(cheat_sheet)

print("🎉 Happy Coding!")
