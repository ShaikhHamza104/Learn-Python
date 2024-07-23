# Implement a function that performs file operations (opening, reading, writing) and uses a finally block to ensure the file is closed properly, regardless of whether an exception occurred.
def openFile(file_name):
    try:
        with open(file_name, 'r') as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("File is not available yet.")
    finally:
        f.close()
def writeFile(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)

try:
    user = int(input('''
1. Open an existing file 
2. Write to a file 
Choose an option: '''))
    
    file_name = input("Enter the file name: ")
    if user == 1:
        openFile(file_name)
    elif user == 2:
        data = input("Input some data for the file: ")
        writeFile(file_name, data)
    else:
        print("Invalid option chosen.")
except ValueError:
    print("Invalid input. Please enter a number.")
