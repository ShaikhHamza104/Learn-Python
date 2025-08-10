#  Write a function that takes a filename as an argument and attempts to open and read the file. Use try, except, and else blocks to handle file operations. If the file is read successfully, print its contents.
import os
d=os.listdir()
for file in d:
    print(file)
try:
    file_name=input("Enter a file name ")
    f=open(file_name)
except FileNotFoundError:
    print("This file name has not present in this directroy")