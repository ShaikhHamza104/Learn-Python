# Initialize the list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Length of the list
print(len(l))  # Output: 9

# Add an element to the end of the list
l.append(10)
print(l)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Insert a new element at a specified position
l.insert(0, 0)
print(l)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Insert a list of elements at the end of the list
l.extend([11, 12, 13, 14, 15])
print(l)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Delete a specific element from the list
l.remove(0)
print(l)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Delete an element based on its index
print(l.pop(9))  # Output: 10
print(l)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]

# Delete an element using the del keyword
del l[0]
print(l)  # Output: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]

# Sort the list in reverse order
l.sort(reverse=True)
print(l)  # Output: [15, 14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2]

# Reverse the list
l.reverse()
print(l)  # Output: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]

# Count the occurrences of an element in the list
print(l.count(2))  # Output: 1

# Copy the list to another list
l2 = l.copy()
print(l2)  # Output: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]

# Clear the copied list
l2.clear()
print(l2)  # Output: []

# Find the index of an element
print(l.index(5))  # Output: 3
