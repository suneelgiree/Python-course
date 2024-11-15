marks = { "Sunil" : 90, "Sunny" : 80, "Sunita" : 70, "Sunit" : 60, "Suniti" : 50, "lists" : [1,2,3,4,5]}

print(marks.items()); # returns a list containing a tuple for each key value pair
print(marks.keys()); # returns a list containing the dictionary's keys
print(marks.values()); # returns a list containing the dictionary's values

marks.update({"Sunil" : 100, "rohan" : "Married"}); # updates the dictionary with the specified key-value pairs
print(marks);

print(marks.get("Sunil")); # returns the value of the specified key