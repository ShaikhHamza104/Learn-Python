#Opening a file 
f=open('random.txt' ,'w')

# writing to a file 
data="I am using File i/o"
f.write(data)

# printing data in file
print(data)

# closeing to a file
f.close()


#Opening a file 
f=open('random.txt' ,'w')

# writing to a file using writelines 
data="I am using File i/o"
f.writelines(data)

# printing data in file
print(data)

# closeing to a file
f.close()