# importing os module : os module is a build in module 
import os

# Removes an empty directory and its parent directories
try:
    os.removedirs('notes/c++')
    print("Directory and subdirectory deleted successfully")

except FileNotFoundError:
    print("Directory and subdirectory does not exists")