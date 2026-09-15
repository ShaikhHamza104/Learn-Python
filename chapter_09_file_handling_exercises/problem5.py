"""
📚 Topic: Chapter 09 Exercise - Problem 5

Censor a list of multiple sensitive words in a text file.

💡 Key points:
    1️⃣ Iterating through a list of forbidden words
    2️⃣ Applying successive replacements to the file content
    3️⃣ Saving the sanitized content back to disk
"""
# . Repeat program 4 for a list of such words to be censored.
words = ["Donkey", "Bander", "Ganda", "Bekar"]
with open("problem4.txt") as f:
    data = f.read()
for word in words:
    data = data.replace(word, "#" * len(word))
with open("problem4.txt", 'w') as f:
    f.write(data)
