"""
📚 Topic: Chapter 06 Exercise - Problem 2

Determine whether a student passes or fails based on individual subject
cutoffs (>= 33%) and overall aggregate percentage (>= 40%).

💡 Key points:
    1️⃣ Calculating overall percentage from three subject scores
    2️⃣ Enforcing compound conditions across total and individual subjects
    3️⃣ Outputting pass or fail status
"""
# 📝 Take marks for the three subjects
mark1 = int(input("Enter your mark for Subject 1: "))
mark2 = int(input("Enter your mark for Subject 2: "))
mark3 = int(input("Enter your mark for Subject 3: "))

# 📊 Calculate total percentage
# Each subject has 100 marks, so total marks = 300
percentage = (100 * (mark1 + mark2 + mark3)) / 300

# 🔍 Check total percentage AND marks in every subject
if percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33:
    print("You are passed 🎉", percentage, "%")

# ❌ If any condition is False, the student fails
else:
    print("You failed. Try again next year 📚", percentage, "%")
