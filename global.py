def fun():
    a = 20
    print(a)

a = 90 # global variable

fun()
print(a)
def fun1():
    global a
    a =50
    print(a)
fun1()