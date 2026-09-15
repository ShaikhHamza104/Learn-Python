"""
📚 Topic: Chapter 04 Exercise - Problem 2

Accept marks of six students from user input and display them in sorted order.

💡 Key points:
    1️⃣ Converting string user inputs to integers
    2️⃣ Storing numerical scores in a list
    3️⃣ Sorting lists in ascending order using `list.sort()`
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
