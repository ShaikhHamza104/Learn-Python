# Write a Python script that reads from a file and writes the content to another file. Use exception handling to manage potential errors such as file not found or permission denied
try:
    file=input("Enter a file name ")
    with open(file, 'r') as f:
        data = f.read()
    copy_file=input("Choose your copy file name : ")
    with open(copy_file,'w') as f:
        f.write(data)
except FileNotFoundError:
    print("File is not available yet.")

except PermissionError:
    print("You can not handle this tasks.")
