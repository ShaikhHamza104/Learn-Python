# importing os module : os module is a build in module 
import os

try:
    os.chdir('example/c')
    file_name = 'main.c'
    #Checks if a path is a file	 
    if os.path.isfile(file_name):
        print(f"File is detected: {file_name}")
    else:
        print(f"File is not detected: {file_name}")
except FileNotFoundError:
    print("Directory not found or file does not exist.")
except OSError as e:
    print(f"Error occurred: {e}")
