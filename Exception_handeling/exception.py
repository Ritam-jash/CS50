# error handeling
""" try:
    x = int(input("what's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an int") """

# TAW
'''try:
    x = int(input("what's is x? "))
except ValueError:
    print("x is not an int")
else:
    print(f"x is {x}")'''

# TAW using loop
'''while True:
    try:
        x = int(input("what's x? "))
        # print(f"x is {x}")
    except ValueError:
        print("x is not an int")
    else:
        break
print(f"x is {x}")'''

# TAW usinf loop
'''while True:
    try:
        x = int(input("what's x? "))
        break
    except ValueError:
        print("x is not an int")
print(f"x is {x}")'''

# TAW using function
""" def main():
    y = get_int()
    print(f"x is {y}")


def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print("x is not an int")
        else:
            break
    return x

main() """


# TAW using function
""" def main():
    y = get_int()
    print(f"new value x is {y}")


def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print("x is not an int")
        else:
            return x
        
main() """


# TAW using NEW PASS function
""" def main():
    y = get_int()
    print(f"new value x is {y}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            pass

main() """


# TAW USING PROMPT NEW function
def main():
    y = get_int("what's x? ")
    print(f"New value of x is {y}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
        