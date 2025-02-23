# get the this type of value (1,000)
x = int(input("what is x?"))
y = int(input("what is y?"))
z = x + y
print(f"{z:,}")

# get the last 2 digit value
x = int(input("what is x?"))
y = int(input("what is y?"))
z = x/y
print(f"{z:.2f}")

# #TAW
x = int(input("what is x?"))
y = int(input("what is y?"))
z = round(x/y,2)
print(f"{z}")

# using strip & title function (remove blank spaces & do first letter capitel)
name = input("what is your name? ").strip() .title()
print(f"Hello, {name}")


# Using function creat a calculator
def main():
    x = int(input("whats is x? "))
    print("x squar is",squar(x))

def squar(n):
    return(n ** 2)

main()


# ccreating normal addition, subtract, multipling, devition FUNCTION
def addition():
    x = int(input("put the x? "))
    y = int(input("put the y? "))
    z = x + y
    print(f"Addition is : {z:,}")

addition()


def subtact():
    x = int(input("put the x? "))
    y = int(input("put the y? "))
    z = x - y
    print(f"subtract is: {z:,}")

subtact()


def multiply():
    x = int(input("put the x? "))
    y = int(input("put the y? "))
    z = x * y
    print(f"multiply is: {z:,}")

multiply()


def devition():
    x = int(input("put the x? "))
    y = int(input("put the y? "))
    z = x / y
    print(f"devition is: {z:.2f}")

devition()


def main():
    name = input("what is your name?")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()


def main():
    x = int(input("what is x? "))
    print("x squar is :", squar(x))

def squar(n):
    return pow(n, 2)

main()