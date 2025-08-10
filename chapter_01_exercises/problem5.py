# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that
import os

# Replace 'path_to_directory' with the path to the directory you want to print
directory_path = '/'

# List the contents of the directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
