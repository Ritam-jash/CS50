# handeling the error
try:
    x = int(input("enter the x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not a integer")


# TAW
try:
    x = int(input("what is x? "))

except ValueError:
    print("x is not a integer")

else:
    print(f"x is {x}")


# TAW USING A LOOP
while True:
    try:
        x = int(input("enter the x? "))
    except ValueError:
        print("x is not a integer")
    else:
        break
print(f"x is {x}")


# TAW
while True:
    try: 
        x = int(input("enter the x? "))
        break
    except ValueError:
        print("x is not a integer")

print(f"x is {x}")


# TAW using a function
def main():
    x = get_num()
    print(f"x is {x}")


def get_num():
    while True:
        try:
            x = int(input("enter the x? "))
        except ValueError:
            print("x is not a integer")
        else:
            return x

main()


# TAW short the code
def main():
    x = get_num()
    print(f"x is {x}")


def get_num():
    while True:
        try:
            return int(input("enter the x? "))
        except ValueError:
            print("x is not a integer")

main()


# TAW solve the problem using promt & pass keyword (shortst way to solve the problem)
def main():
    x = get_number("what is x? ")
    print(f"x is {x}")

def get_number(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            pass

main()


# Practices
def main():
    x = get_number("what is x ? ")
    print(f"x is {x}")


def get_number(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            pass

main()