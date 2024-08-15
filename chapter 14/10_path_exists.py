# importing os module : os module is a build in module 
import os
os.chdir('example/c')

file_name='main.c'

# Checks if a path exists	
if os.path.exists('main.c'):
    print(f"Yes, {file_name} file is exists")
else:
    print(f"No, {file_name} file is exists")
