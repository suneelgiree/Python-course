a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b == 0:
    raise ValueError("Please enter a number other than 0")
else:
 print(f"Division of a and b:{a/b}")