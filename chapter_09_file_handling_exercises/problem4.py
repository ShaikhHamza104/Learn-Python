"""
📚 Topic: Chapter 09 Exercise - Problem 4

Censor occurrences of a forbidden word ('Donkey') in a text file by replacing
them with '######'.

💡 Key points:
    1️⃣ Reading file content into memory
    2️⃣ Replacing target words with `str.replace()`
    3️⃣ Writing updated text back to the file
"""
# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.
with open('problem4.txt', 'r')as f:
    data = f.read()
    data = data.replace("Donkey", "#####")
    # data=data.replace("#####","Donkey")


with open('problem4.txt', 'w')as f:
    f.write(f"{data}")
