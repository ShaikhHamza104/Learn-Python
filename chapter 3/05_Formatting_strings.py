# Assigning string value "Hamza" to the variable 'name'
name = "Hamza"

# Assigning integer value 18 to the variable 'age'
age = 18

# Method 1: Using the old-style % formatting to insert variables into strings
# %s is a placeholder for a string, and %d is a placeholder for a decimal (integer).
# The variables to substitute are provided as a tuple after the % symbol.
print("The name of student is %s and age is %d " % (name, age))

# Method 2: Using the str.format() method, which is more versatile and readable than % formatting.
# Curly braces {} are placeholders for the variables to be formatted.
# The format() method takes arguments, 'name' and 'age', and places them in the respective placeholders.
print("The name of student is {} and age is {} ".format(name, age))

# Method 3: Using f-string (formatted string literals) introduced in Python 3.6
# It's an even more readable and concise way to include expressions inside string literals.
# Variables are directly embedded in curly braces.
print(f"The name of student is {name} and age is {age} ")
