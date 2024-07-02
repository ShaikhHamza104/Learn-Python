#Opening a file 
f=open('sample.txt' ,'r')

# reading to a file 
data=f.read()

# printing data in file
print(data)

# closeing to a file
f.close()


#Opening a file 
f=open('sample.txt' ,'r')

# reading  one line file using readline
data=f.readline()

# printing data in file
print(data)

# closeing to a file
f.close()


#Opening a file 
f=open('sample.txt' ,'r')

# reading  file in a form of list  using readlines
data=f.readlines()

# printing data in file
print(data)

# closeing to a file
f.close()
