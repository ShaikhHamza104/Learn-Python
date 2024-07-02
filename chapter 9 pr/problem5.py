# . Repeat program 4 for a list of such words to be censored.
words=["Donkey","Bander","Ganda","Bekar"]
with open("problem4.txt") as f:
    data=f.read()
for word in words:
    data=data.replace(word,"#"*len(word))
with open("problem4.txt", 'w') as f:
    f.write(data)