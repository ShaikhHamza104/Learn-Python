# importing os module : os module is a build in module 
import os
os.chdir('example/c')
file_name='main.c'
files=[]
try:
    # Deletes a file	

    os.remove(file_name)
except PermissionError:
    print("You have not permition to delete a file")