"""
📚 Topic: Chapter 04 Exercise - Problem 1

Store seven fruit names entered by the user into a list and display them.

💡 Key points:
    1️⃣ Taking user input sequentially
    2️⃣ Appending items dynamically using `list.append()`
    3️⃣ Displaying the populated list
"""
# 🍎 Create an empty list to store the fruit names
fruits = []


# 1️⃣ Take the first fruit from the user
# append() adds the entered fruit to the end of the list.
f1 = input("Enter Fruit name : ")
fruits.append(f1)


# 2️⃣ Take the second fruit and add it to the list
f2 = input("Enter Fruit name : ")
fruits.append(f2)


# 3️⃣ Take the third fruit and add it to the list
f3 = input("Enter Fruit name : ")
fruits.append(f3)


# 4️⃣ Take the fourth fruit and add it to the list
f4 = input("Enter Fruit name : ")
fruits.append(f4)


# 5️⃣ Take the fifth fruit and add it to the list
f5 = input("Enter Fruit name : ")
fruits.append(f5)


# 6️⃣ Take the sixth fruit and add it to the list
f6 = input("Enter Fruit name : ")
fruits.append(f6)


# 7️⃣ Take the seventh fruit and add it to the list
f7 = input("Enter Fruit name : ")
fruits.append(f7)


# 📋 Print the final list containing all seven fruits
print(fruits)
