# Gernate 10 element in list using "list comprehension"
l=[i for i in range(1,11)]
print(l)

# Gernate even element from 10 to 40 in list using "list comprehension"
l=[i for i in range(10,41) if i%2==0]
print(l)

# Gernate odd element from 10 to 20 in list using "list comprehension"
l=[i for i in range(10,21) if i%2!=0]
print(l)
