"""
📚 Topic: deque

This script demonstrates deque from Python's collections module.

💡 Key points:
    1. Creating a deque
    2. append()
    3. pop()
    4. popleft()
    5. extend()
    6. extendleft()
    7. appendleft()
    8. maxlen

🧠 Beginner tip:
    deque supports efficient insertion and removal from both
    ends of the collection.
"""

from collections import deque


# ============================================================
# 1. BASIC LIST
# ============================================================

print("=" * 60)
print("1. BASIC LIST")
print("=" * 60)

numbers = list(range(1, 6))

print("Numbers:", numbers)


# ============================================================
# 2. LIST APPEND AND POP
# ============================================================

print("\n" + "=" * 60)
print("2. LIST APPEND AND POP")
print("=" * 60)

numbers.append(6)
print("After append:", numbers)

numbers.pop()
numbers.pop()

print("After two pop operations:", numbers)


# ============================================================
# 3. BASIC DEQUE
# ============================================================

print("\n" + "=" * 60)
print("3. BASIC DEQUE")
print("=" * 60)

items = deque(numbers)

print("Deque:", items)


# ============================================================
# 4. APPEND
# ============================================================

print("\n" + "=" * 60)
print("4. APPEND")
print("=" * 60)

items.append(6)

print("After append:", items)


# ============================================================
# 5. POP
# ============================================================

print("\n" + "=" * 60)
print("5. POP")
print("=" * 60)

items.pop()

print("After pop:", items)


# ============================================================
# 6. POPLEFT
# ============================================================

print("\n" + "=" * 60)
print("6. POPLEFT")
print("=" * 60)

items.popleft()

print("After popleft:", items)


# ============================================================
# 7. EXTEND
# ============================================================

print("\n" + "=" * 60)
print("7. EXTEND")
print("=" * 60)

numbers.extend([6, 7, 8])

print("List after extend:", numbers)


# ============================================================
# 8. EXTENDLEFT
# ============================================================

print("\n" + "=" * 60)
print("8. EXTENDLEFT")
print("=" * 60)

items = deque(range(1, 6))

items.extendleft([0, -1, -2])

print("After extendleft:", items)


# ============================================================
# 9. APPENDLEFT
# ============================================================

print("\n" + "=" * 60)
print("9. APPENDLEFT")
print("=" * 60)

items.appendleft(-3)

print("After appendleft:", items)


# ============================================================
# 10. MAXLEN
# ============================================================

print("\n" + "=" * 60)
print("10. MAXLEN")
print("=" * 60)

limited_items = deque(range(1, 4), maxlen=5)

print("Initial:", limited_items)

limited_items.append(4)
print("After append:", limited_items)

limited_items.extend([5, 6, 7, 8])
print("After extend:", limited_items)

limited_items.appendleft(3)
print("After appendleft:", limited_items)


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("deque examples completed!")
print("=" * 60)
