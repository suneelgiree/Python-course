# program to find the factorial of a number using recursion
def recursion(n):
    if n == 0:
        return 1
    return n*recursion(n-1)

a = int(input("Enter a number: "))
rec = recursion(a)
print(rec)
