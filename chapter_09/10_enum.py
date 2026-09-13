"""
📚 Topic: Enum

This script demonstrates Python Enums using the enum module.

💡 Key points:
    1. Basic Enum creation
    2. Enum names and values
    3. str() vs repr()
    4. Converting Enum members
    5. Enum properties
    6. Iteration and identity
    7. Membership and comparisons
    8. Getting members by value and key
    9. auto() values
    10. @unique decorator
    11. Real-life logging example

🧠 Beginner tip:
    Run this file section by section.
    Change one value and run it again to understand
    how Enum members behave.
"""

# ============================================================
# 1. BASIC ENUM
# ============================================================

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print("=" * 60)
print("1. BASIC ENUM")
print("=" * 60)

print(type(Color))
print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)


# ============================================================
# 2. ENUM NAME AND VALUE
# ============================================================

print("\n" + "=" * 60)
print("2. ENUM NAME AND VALUE")
print("=" * 60)

# Every Enum member has a name and a value.

print("RED name:", Color.RED.name)
print("GREEN name:", Color.GREEN.name)
print("BLUE name:", Color.BLUE.name)

print("RED value:", Color.RED.value)
print("GREEN value:", Color.GREEN.value)
print("BLUE value:", Color.BLUE.value)


# ============================================================
# 3. STR VS REPR
# ============================================================

print("\n" + "=" * 60)
print("3. STR VS REPR")
print("=" * 60)

print("str:", str(Color.RED))
print("repr:", repr(Color.RED))

print("str:", str(Color.GREEN))
print("repr:", repr(Color.GREEN))

print("str:", str(Color.BLUE))
print("repr:", repr(Color.BLUE))


# ============================================================
# 4. ENUM WITH LIST, TUPLE, DICT AND SET
# ============================================================

print("\n" + "=" * 60)
print("4. ENUM WITH COLLECTIONS")
print("=" * 60)

# List of Enum members
print("List:", list(Color))

# Tuple of Enum members
print("Tuple:", tuple(Color))

# Dictionary containing names and values
color_dict = {color.name: color.value for color in Color}
print("Dictionary:", color_dict)

# Set of Enum members
print("Set:", set(Color))


# ============================================================
# 5. ORDER OF EXECUTION
# ============================================================

print("\n" + "=" * 60)
print("5. ORDER OF EXECUTION")
print("=" * 60)

# Enum members are iterated in the order
# in which they are defined in the class.

for color in Color:
    print(color)


# ============================================================
# 6. ENUM PROPERTIES
# ============================================================

print("\n" + "=" * 60)
print("6. ENUM PROPERTIES")
print("=" * 60)

# Enum members are immutable.
#
# The following would raise AttributeError:
#
# Color.BLUE.value = 1000

print("Color.BLUE value:", Color.BLUE.value)


# ============================================================
# 7. HASHABLE
# ============================================================

print("\n" + "=" * 60)
print("7. HASHABLE")
print("=" * 60)

# Enum members are hashable.
# Therefore, they can be used as dictionary keys.

color_dict = {}

for color in Color:
    color_dict[color] = color.value

print("Color dictionary:", color_dict)


# ============================================================
# 8. ITERATION
# ============================================================

print("\n" + "=" * 60)
print("8. ITERATION")
print("=" * 60)

for color in Color:
    print(color)


# ============================================================
# 9. IDENTITY
# ============================================================

print("\n" + "=" * 60)
print("9. IDENTITY")
print("=" * 60)

print("RED id:", id(Color.RED))
print("GREEN id:", id(Color.GREEN))
print("BLUE id:", id(Color.BLUE))

print("RED is GREEN:", Color.RED is Color.GREEN)


# ============================================================
# 10. COMPARISON OPERATORS
# ============================================================

print("\n" + "=" * 60)
print("10. COMPARISON OPERATORS")
print("=" * 60)

# Equality comparison
print("RED == GREEN:", Color.RED == Color.GREEN)

# Inequality comparison
print("RED != GREEN:", Color.RED != Color.GREEN)

# Normal Enum members do not support ordering comparisons.
#
# The following operations raise TypeError:
#
# Color.RED < Color.GREEN
# Color.RED > Color.GREEN
# Color.RED <= Color.GREEN
# Color.RED >= Color.GREEN


# ============================================================
# 11. MEMBERSHIP OPERATOR
# ============================================================

print("\n" + "=" * 60)
print("11. MEMBERSHIP OPERATOR")
print("=" * 60)

print("RED in Color:", Color.RED in Color)
print("GREEN in Color:", Color.GREEN in Color)
print("BLUE in Color:", Color.BLUE in Color)


# ============================================================
# 12. GET MEMBER THROUGH VALUE
# ============================================================

print("\n" + "=" * 60)
print("12. GET MEMBER THROUGH VALUE")
print("=" * 60)

# Pass the value to the Enum class.

print(Color(1))
print(Color(2))
print(Color(3))


# ============================================================
# 13. GET MEMBER THROUGH KEY
# ============================================================

print("\n" + "=" * 60)
print("13. GET MEMBER THROUGH KEY")
print("=" * 60)

# Use the member name as a key.

print(Color["RED"])
print(Color["GREEN"])
print(Color["BLUE"])

# upper() can be useful when the input is lowercase.

color_name = "red"
print(Color[color_name.upper()])


# ============================================================
# 14. GET MEMBER THROUGH ATTRIBUTE
# ============================================================

print("\n" + "=" * 60)
print("14. GET MEMBER THROUGH ATTRIBUTE")
print("=" * 60)

print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)


# ============================================================
# 15. AUTO VALUES
# ============================================================

print("\n" + "=" * 60)
print("15. AUTO VALUES")
print("=" * 60)

from enum import auto  # noqa: E402


class Week(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


print("Member:", Week.MONDAY)
print("Value:", Week.MONDAY.value)
print("Name:", Week.MONDAY.name)


# ============================================================
# 16. MANUAL VALUE + AUTO
# ============================================================

print("\n" + "=" * 60)
print("16. MANUAL VALUE + AUTO")
print("=" * 60)


class Weakness(Enum):
    MONDAY = 10
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


print("MONDAY value:", Weakness.MONDAY.value)
print("MONDAY name:", Weakness.MONDAY.name)

print("TUESDAY value:", Weakness.TUESDAY.value)
print("TUESDAY name:", Weakness.TUESDAY.name)


# ============================================================
# 17. UNIQUE ENUM VALUES
# ============================================================

print("\n" + "=" * 60)
print("17. UNIQUE ENUM VALUES")
print("=" * 60)

from enum import unique  # noqa: E402


@unique
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = auto()


print("Monday:", Weekday.MONDAY)
print("Sunday:", Weekday.SUNDAY)

# @unique prevents duplicate values.
#
# Example:
#
# @unique
# class InvalidWeekday(Enum):
#     MONDAY = 1
#     SUNDAY = 1
#
# This raises ValueError.


# ============================================================
# 18. REAL-LIFE EXAMPLE
# ============================================================

print("\n" + "=" * 60)
print("18. REAL-LIFE EXAMPLE: LOGGING")
print("=" * 60)


class Debug(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


def log(level, message):
    """Print messages starting from INFO level."""
    if level.value >= Debug.INFO.value:
        print(f"[{level.name}]: {message}")


log(Debug.DEBUG, "This is a debug message")
log(Debug.INFO, "This is an info message")
log(Debug.WARNING, "This is a warning message")
log(Debug.ERROR, "This is an error message")
log(Debug.CRITICAL, "This is a critical message")


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("Enum examples completed!")
print("=" * 60)
