name="hamza"
# string are immutable
# To find the length of string  
print(len(name))

# To find the start of the string 
print(name.startswith("Ha"))

# To find the end of the string 
print(name.endswith("za"))

# to convert string of all character in upper case 
print(name.upper())

# to convert string of all character in lower case 
print(name.lower())

# to convert first character in upper case latter 
print(name.capitalize())

# to find the first occurance latter 
print(name.find("a",0))

# Check if all characters in the string are alphanumeric (letters and numbers)
print(name.isalnum())

# to find the number of occurance 
print(name.count("a"))

# to find the index of character in fist occurance 
print(name.index("z"))

# check that the string has contain character 
print(name.isalpha()) 

# check that the string has contain number 
print(name.isdigit())

# to replace character 
print(name.replace("h","H"))

s="         Python                       "
# Remove leading and trailing whitespaces from the string
print(s.strip())

s="Python programming language"
#  splits the string "s" into a list of words 
print(s.split())

# Make the first letter in each word upper case:
print(s.title())#Python Programming Language