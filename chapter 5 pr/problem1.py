# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words={
    "Kitab":"Book",
    "riyazi":"Math",
    "Dabba":"Box",
    "Rabber":"erazer",
    "maded":"help",
    "billi":"cat"
}
word=input("Enter a word : ").capitalize()
print(words.get(word))