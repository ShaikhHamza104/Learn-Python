"""
📚 Topic: Chapter 04 Exercise - Problem 2

This script demonstrates chapter 04 exercise - problem 2 using user input
and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 04 exercise - problem 2
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 04 exercise - problem 2 affects the result.
"""


# 👨‍🎓 Take marks of the first student
student1 = int(input("Enter mark of student 1 "))


# 👨‍🎓 Take marks of the second student
student2 = int(input("Enter mark of student 2 "))


# 👨‍🎓 Take marks of the third student
student3 = int(input("Enter mark of student 3 "))


# 👨‍🎓 Take marks of the fourth student
student4 = int(input("Enter mark of student 4 "))


# 👨‍🎓 Take marks of the fifth student
student5 = int(input("Enter mark of student 5 "))


# 👨‍🎓 Take marks of the sixth student
student6 = int(input("Enter mark of student 6 "))


# 📋 Store all students' marks inside a list
mark_of_student = [student1, student2, student3, student4, student5, student6]


# 🔢 Sort the marks in ascending order
# sort() changes the original list and arranges the values
# from the smallest mark to the largest mark.
mark_of_student.sort()


# 📊 Display the sorted marks
print(mark_of_student)
