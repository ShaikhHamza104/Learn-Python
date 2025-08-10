'''
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
'''
import os
dr=os.chdir('chapter 9 pr/table')

def function():
    n=21
    for i in range(2,n):
        with open(f"table{i}.txt" ,'a') as f:
            for j in range(1,11):
                f.write(f"{i} × {j} = {i * j}\n")
                
function()
