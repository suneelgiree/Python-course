# a set is a collection of non-repetitive elements. It is a collection of unique elements.

d = {} # empty dictionary

# s = {1, 2, 3, 4, 5,1,1,1,1} # set with 5 elements
s = set() # empty set
print(type(s))

# adding elements to a set
s.add(1)
s.add(2)
s.add(2) # adding a value repeatedly does not change the set
print(s)

# removing elements from a set
s.remove(2) # removes 2 from the set
print(s)