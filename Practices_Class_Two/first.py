name = input("What is your name? ").strip().upper()
print(F"My name is {name}")



# Round figure
x = float(input("enter the x? "))
y = float(input("enter the Y? "))

z = round(x + y)

print(f"{z: ,}")




# round function
def devision():
    x = float(input("what is x? "))
    y = float(input("what is y? "))
    z = round(x/y, 2)
    print(z)

devision()




# TAW
def multiplication():
    x = float(input("what is x? "))
    y = float(input("what is y? "))
    z = x * y
    print(f"value is {z: .2f}")

multiplication()




# squar function
def squar():
    x = float(input("enter the value? "))
    z =x ** 2
    print(f"squar is {z: .4f}")

squar()




# write a squar function
def main():
    x = int(input("enter the x? "))
    print("the squar is",squar(x))


def squar(n):
    return n ** 2


if __name__== "__main__":
    main()


# craete a hello function
def main():
    name = input("enter your name? ")
    hello(name)


def hello(to = "world"):
    print("helloo",to)

if __name__ == "__main__":
    main()

def main():
    name = input("what is your name?")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()



# even number
def main():
    x = int(input("what is x? "))
    if x_even(x):
        print("even")
    else:
        print("odd")


def x_even(n):
    if n % 2 == 0:
        return True
    # else:
    #     return False
    
if __name__ == "__main__":
    main()


# reminder time
def main():
    time = input("what is time right now? (HH:MM)")
    hour = convert(time)
    if 7 <= hour <= 8:
        print(f"Now brakfast time{hour}")
    elif 12 <= hour <= 13:
        print(f"Lunch time{hour}")
    elif 21 <= hour <= 22:
        print(f"Dinner time{hour}")
    else:
        print("enter a valid time")


def convert(time):
    hour, minites = time.split(":")
    return int(hour) + int(minites)/60

if __name__ == "__main__":
    main()