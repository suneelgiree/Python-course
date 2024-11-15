a = input("Enter a number: ") #input function is used to take input from the user as a string

b= input("Enter another number: ")

print("The first number is: ", a)
print("The second number is: ", b)

print(a + b) #addition '''addition isnot possible because the input function returns a string and '+' operator is used for concatenation of strings so the output will be the concatenation of the two strings'''

#to prevent this we can typecast the input to an integer

c = int(input("Enter a number: ")) #input function is used to take input from the user as a string
d = int(input("Enter another number: "))

print(c + d)