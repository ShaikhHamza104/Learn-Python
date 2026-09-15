"""
📚 Topic: Exercise 1 - Collecting Strings in a List

This exercise prompts the user for multiple fruit names using `input()`,
appends each entered string into a list, and displays the populated list.

💡 Key points:
    1️⃣ Initializing an empty list container (`fruits = []`)
    2️⃣ Gathering terminal user inputs with `input()`
    3️⃣ Storing strings sequentially using the `.append()` list method

🧠 Beginner tip:
    Lists maintain insertion order, making them ideal for collecting items
    entered one-by-one by a user.
"""

# 🍎 Create an empty list to store the fruits
fruits = []


# 1️⃣ Take the first fruit from the user and add it to the list
f1 = input("Enter Fruit name : ")
fruits.append(f1)


# 2️⃣ Take the second fruit from the user and add it to the list
f2 = input("Enter Fruit name : ")
fruits.append(f2)


# 3️⃣ Take the third fruit from the user and add it to the list
f3 = input("Enter Fruit name : ")
fruits.append(f3)


# 4️⃣ Take the fourth fruit from the user and add it to the list
f4 = input("Enter Fruit name : ")
fruits.append(f4)


# 5️⃣ Take the fifth fruit from the user and add it to the list
f5 = input("Enter Fruit name : ")
fruits.append(f5)


# 6️⃣ Take the sixth fruit from the user and add it to the list
f6 = input("Enter Fruit name : ")
fruits.append(f6)


# 7️⃣ Take the seventh fruit from the user and add it to the list
f7 = input("Enter Fruit name : ")
fruits.append(f7)


# 📋 Print the final list containing all seven fruits
print(fruits)
