a = {1, 2, 3, 4, 5,1,1,1,1, " Sunil "}
a.add(1000)
print(type(a))
print(a)

s = set() # empty set
s.add(1) # adding a value repeatedly does not change the set
s.add(2)    
s.add(2)
print(s)

s.remove(2) # removes 2 from the set
print(s)

print(len(a))