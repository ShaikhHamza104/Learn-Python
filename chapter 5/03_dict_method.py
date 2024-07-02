# Dictionary of marks
mark = {
    "Rohan": 70,
    "Harry": 100,
    "Sonali": 80,
    "Mari": 75,
    "Yusuf": 95
}

# Print all keys in the dictionary
print(mark.keys())  # Output: dict_keys(['Rohan', 'Harry', 'Sonali', 'Mari', 'Yusuf'])

# Print all values in the dictionary
print(mark.values())  # Output: dict_values([70, 100, 80, 75, 95])

# Print all key-value pairs in the dictionary
print(mark.items())  # Output: dict_items([('Rohan', 70), ('Harry', 100), ('Sonali', 80), ('Mari', 75), ('Yusuf', 95)])

# Get the value associated with the key "Yusuf"
print(mark.get("Yusuf"))  # Output: 95

# Update the dictionary with new key-value pairs, or update existing keys
mark.update({"Yusuf": 99, "Renuka": 95})
print(mark)  # Output: {'Rohan': 70, 'Harry': 100, 'Sonali': 80, 'Mari': 75, 'Yusuf': 99, 'Renuka': 95}

# Remove and return the value associated with the key "Rohan"
# print(mark.pop("Rohan"))  # Uncommenting this will output: 70

# Remove and return the last inserted key-value pair
print(mark.popitem())  # Output: ('Renuka', 95)

# Copy the dictionary to a new dictionary
my_mark = mark.copy()
print(my_mark)  # Output: {'Rohan': 70, 'Harry': 100, 'Sonali': 80, 'Mari': 75, 'Yusuf': 99}

# Clear all elements from the copied dictionary
my_mark.clear()
print(my_mark)  # Output: {}

# Delete the copied dictionary
del my_mark

# Set default value for the key "Mukesh"
mark.setdefault("Mukesh", 70)
print(mark)  # Output: {'Rohan': 70, 'Harry': 100, 'Sonali': 80, 'Mari': 75, 'Yusuf': 99, 'Mukesh': 70}