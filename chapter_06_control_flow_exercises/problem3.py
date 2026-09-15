"""
📚 Topic: Chapter 06 Exercise - Problem 3

Detect spam comments by checking for known promotional keywords and phrases.

💡 Key points:
    1️⃣ Defining a list of spam indicator keywords
    2️⃣ Using the `in` membership operator against user input text
    3️⃣ Flagging suspicious comments
"""
# 🚨 Store the spam phrases
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

# 💬 Ask the user to enter a comment
comment = input("Enter your comment: ")

# 🔍 Check whether any spam phrase is present in the comment
if p1 in comment or p2 in comment or p3 in comment or p4 in comment:
    print("Spam is detected 🚨")

# ✅ If none of the spam phrases are found
else:
    print("This comment is not spam ✅")
