# importing os module : os module is a build in module 
import os

# Creates a directory and its parent directories if they don't exist
try:
    os.makedirs('example/C/main.c')
    print("Directory created successfully")

except FileExistsError as e:
    print("Directory already exists")