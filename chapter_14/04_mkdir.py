# importing os module : os module is a build in module 
import os

# Creates a new directory
try:
    os.mkdir('example')
    print("Directory created successfully")

except FileExistsError as e:
    print("Directory already exists")
