s1 = {1, 45, 6, 7, 8, 9}
s2 = {1, 2, 3, 4, 5, 6}

# union of two sets
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 45}

# intersection of two sets
print(s1.intersection(s2)) # {1, 6}

print(s1.difference(s2)) # {8, 9, 45, 7}
print(s2.difference(s1)) # {2, 3, 4, 5}