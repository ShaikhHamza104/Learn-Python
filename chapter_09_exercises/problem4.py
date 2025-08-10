# A file contains a word “Donkey” multiple times. You need to write a program  which replace this word with ##### by updating the same file. 
with open ('problem4.txt','r')as f:
    data=f.read()
    data=data.replace("Donkey","#####")
    # data=data.replace("#####","Donkey")


with open ('problem4.txt','w')as f:
        f.write(f"{data}")