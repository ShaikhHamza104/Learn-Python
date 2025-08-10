# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open("poems.txt") as f:
    data=f.read()
    if 'twinkle' in data:
        print("file contain 'Twinkle' ")
        