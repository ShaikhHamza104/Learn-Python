s={1,2,10,18,17,90}

# add an element in set
s.add(100)
print(s)

# add multiple element in set 
s.update({3,4,5})
print(s)

# remove one element in set
s.remove(1)
print(s)

# remove one element in set
s.discard("100")
print(s)

# remove random element in set 
s.pop()
print(s)

# copy one set into onthor set
s1=s.copy()
print(s1)

# clear s1 
s1.clear()
print(s1)