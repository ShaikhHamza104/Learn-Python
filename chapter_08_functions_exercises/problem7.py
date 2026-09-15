"""
📚 Topic: Chapter 08 Exercise - Problem 7

Write a python function to remove a specified word from a list and strip it
at the same time.

💡 Key points:
    1️⃣ Filtering target words out of a sequence
    2️⃣ Stripping unwanted characters from remaining elements
    3️⃣ Returning a clean new list
"""


# Write a python function to remove a given word from a list and strip it at
# the same time


def remove_and_strip(words_list, word):
    result = []
    for item in words_list:
        if item != word:
            result.append(item.strip(word))
    return result


words = ["Harry", "Rohan", "Roshi", "an"]
print(remove_and_strip(words, "an"))
