# create a addition function using formate(f) string
def addition ():
    x = float(input("enter the value of x: "))
    y = float(input("enter the value of y: "))
    z = round(x + y)
    print(f"{z : ,}")

addition()


# create a devision function using f string
def devsion_num():
    a = float(input("enter the value of a: "))
    b = float(input("enter the value of b: "))
    c = a / b
    print(f"{c : .4f}")

devsion_num()


# Another wayusing round method
def devsion_num():
    e = float(input("enter the value of e: "))
    f = float(input("enter the value of f: "))
    g = round(e /f , 2)
    print(g)

devsion_num()


# square of a float number
def square():
    x = float(input("enter the value of x: "))
    z = x ** 2
    print(f"{z : .5f}")

square()