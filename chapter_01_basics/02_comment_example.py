"""
📚 Topic: Comments & Documentation in Python

This script explains how to document code effectively using single-line
comments (`#`), inline explanations, multi-line blocks, and docstrings. Clear
comments explain *why* code exists, helping teammates and your future self
understand the intent behind implementations.

💡 Key points:
    1️⃣ Using `#` for single-line comments and inline notes
    2️⃣ Documenting logic with multi-line commented explanations
    3️⃣ Commenting out code temporarily during testing and debugging

🧠 Beginner tip:
    Good comments explain the *why*, not the *what*. Write code that is
    self-explanatory, and reserve comments for non-obvious reasoning.
"""


print("Hello World!")  # This comment is at the end of a line

# You can use comments to explain what your code does:
# The line below prints my name
print("My name is Hamza Shaikh")  # This is an inline comment


# ============================================================
# 2️⃣ WHY USE COMMENTS? 🤔
# ============================================================

# ✅ Reason 1: Explain your code
# Calculate the area of a rectangle
length = 10
width = 5
area = length * width
print("Area =", area)

# ✅ Reason 2: Make code readable for others (and future you!)
# This variable stores the user's age
user_age = 20

# ✅ Reason 3: Temporarily disable code (commenting out)
# print("This line won't run because it's commented out")
print("This line WILL run!")


# ============================================================
# 3️⃣ MULTI-LINE COMMENTS (Using Multiple #)
# ============================================================
# Python doesn't have a special multi-line comment syntax,
# but you can use multiple single-line comments like this:

# This is a multi-line comment
# It spans across several lines
# Each line starts with a # symbol
# This is great for longer explanations!

print("Multi-line comments help explain complex code!")


# ============================================================
# 4️⃣ MULTI-LINE STRINGS AS COMMENTS (Docstrings) 📝
# ============================================================
# You can also use triple quotes """ or '''
# Python ignores these if they're not assigned to a variable
# These are often used for documentation

"""
This is a multi-line string.
Python will read it but ignore it if not stored in a variable.
Many developers use this for longer explanations
or at the beginning of files/functions.
"""

"""
You can use single quotes too!
Both work the same way.
"""

print("Docstrings are useful for documentation!")


# ============================================================
# 5️⃣ INLINE COMMENTS (At the End of a Line) ➡️
# ============================================================
# Be careful not to overuse these - keep them short!

x = 10  # Store the value 10 in variable x
y = 20  # Store the value 20 in variable y
sum_xy = x + y  # Add x and y together
print(sum_xy)  # Print the result


# ============================================================
# 6️⃣ COMMENTING OUT CODE (Debugging Trick) 🐛
# ============================================================
# Sometimes you want to stop a line from running without deleting it
# Just add # at the beginning!

# print("This won't print")
print("But this WILL print!")

# You can comment out multiple lines:
# name = "John"
# age = 25
# print(name, age)

print("Commenting is a great debugging tool!")


# ============================================================
# 7️⃣ BEST PRACTICES FOR COMMENTS ⭐
# ============================================================

# ✅ DO:
# - Write clear, simple comments
# - Explain WHY, not just WHAT (the code shows what)
# - Update comments when you change code
# - Use comments to separate sections of code

# ❌ DON'T:
# - Don't write obvious comments:  x = 5  # Set x to 5 (too obvious!)
# - Don't leave old, outdated comments
# - Don't use comments to hide messy code - fix the code instead!


# ============================================================
# 🎯 PRACTICE TIME!
# ============================================================
# Try these exercises:

# Exercise 1: Add a comment explaining this line
# (Write your comment below)
# _______________________________
print("I love Python!")

# Exercise 2: Comment out the line below so it doesn't run
# print("Hide me!")

# Exercise 3: Write a multi-line comment about what you learned today
# (Write your comment below using # on each line)
# _______________________________
# _______________________________
# _______________________________


# ============================================================
# 🎉 SUMMARY
# ============================================================
# #         → Single-line comment
# """ """   → Multi-line string (can be used as comment)
# Comments make your code readable and maintainable!
# ============================================================

print("\n🎊 Great job learning about comments! 🎊")
print("Remember: Good code with good comments = Happy developers! 😊")
