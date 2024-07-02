# 2. Write a program to accept marks of 6 students and display them in a sorted manner
student1=int(input("Enter mark of student 1 "))
student2=int(input("Enter mark of student 2 "))
student3=int(input("Enter mark of student 3 "))
student4=int(input("Enter mark of student 4 "))
student5=int(input("Enter mark of student 5 "))
student6=int(input("Enter mark of student 6 "))
mark_of_student=[student1,student2,student3,student4,student5,student6]
mark_of_student.sort()
print(mark_of_student)