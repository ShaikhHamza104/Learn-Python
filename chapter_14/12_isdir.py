# importing os module : os module is a build in module 
import os

try:
    os.chdir('example')
    dir_name = 'c'
    # Checks if a path is a directory	
    if os.path.isdir(dir_name):
        print(f"directory is detected: {dir_name}")
    else:
        print(f"directory is not detected: {dir_name}")
except FileNotFoundError:
    print("Directory not found or file does not exist.")
except OSError as e:
    print(f"Error occurred: {e}")
