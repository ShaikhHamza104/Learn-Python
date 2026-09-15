"""
📚 Topic: Chapter 04 Exercise - Problem 5

Count the total number of zeros in a given tuple: `(7, 0, 8, 0, 0, 9)`.

💡 Key points:
    1️⃣ Initializing an immutable numerical tuple
    2️⃣ Using `tuple.count(value)` to tally occurrences
    3️⃣ Printing the occurrence count
"""
# 📦 Create a tuple containing numbers
# Notice that the number 0 appears three times.
a = (7, 0, 8, 0, 0, 9)


# 🔢 Count how many times 0 appears in the tuple
# count(0) checks the entire tuple and returns the total number
# of occurrences of the value 0.
count = a.count(0)


# 📊 Display the number of zeros
print(count)

# Output:
# 3
