"""
📚 Topic: Chapter 06 Exercise - Problem 7

Check whether a social media post mentions a specific target person,
performing case-insensitive search.

💡 Key points:
    1️⃣ Normalizing text case with `.lower()`
    2️⃣ Substring search using `in`
    3️⃣ Reporting whether the subject is mentioned
"""
# 👤 Store the name we want to search for
name = "Harry"

# 💬 Ask the user to enter their post
post = input("Enter your post: ")

# 🔍 Check whether "Harry" is present in the post
# 🔤 lower() makes the search case-insensitive
if name.lower() in post.lower():
    print('This post is talking about "Harry"')

# ❌ If Harry is not mentioned
else:
    print('This post is not talking about "Harry"')
