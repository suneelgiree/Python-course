a = "Suneel";

b = len(a); # len() function is used to get the length of the string
print(b);

print(a.endswith("eel")); # endswith() function is used to check if the string ends with the specified value
print(a.endswith("eal")); # False

print(a.count("e")); # count() function is used to count the number of times a specified value occurs in a string

print(a.startswith("Sun")); # startswith() function is used to check if the string starts with the specified value
print(a.startswith("sun")); # False

print(a.capitalize()); # capitalize() function is used to convert the first character of the string to uppercase

word_replace = a.replace("Sun", "pran"); # replace() function is used to replace a specified value with another value in a string
print(word_replace);