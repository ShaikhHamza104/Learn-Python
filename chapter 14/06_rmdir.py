# importing os module : os module is a build in module 
import os

# Removes an empty directory
try:
    os.rmdir('example')
    print("Directory deleted successfully")

except FileNotFoundError:
    print("Directory does not exists")
except OSError:
    print("The directory is not empty: 'example'")
