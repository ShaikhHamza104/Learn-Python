'''
8. Write a program to print the following star pattern:
*
**
*** for n = 3
'''
# Define the number of rows
n = 3

# Loop through each row
for i in range(1, n + 1):
    # Print '*' i times for the current row
    for j in range(i):
        print("*", end='')
    # Print a newline after each row
    print()
