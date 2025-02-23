# Finding a even number
""" x = int(input("what is x? "))

if x % 2 == 0 :
    print("X is a even number")
else:
    print("x is a odd number") """


# Using a function find a even number
''' def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main() '''


# Using a function find a even number TAW
''' def main():
    x = int(input("what is x? "))
    if is_even (x):
        print("Even number")
    else:
        print("Odd number")

def is_even(n):
    return True if n % 2 == 0 else False

main() '''


# Using a function find a even number TAW (shortest way)
def main():
    x = int(input("what is x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()