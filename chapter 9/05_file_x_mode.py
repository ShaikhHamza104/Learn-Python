# 'x' mode give error if file is alrady exisist 
# open a file in x mode
f=open("random1.txt",'x')

# data input from the user
data=input("Enter data")

# writing to a file 
f.write(data)

# printing data
print(data)

# closing to a file
f.close()