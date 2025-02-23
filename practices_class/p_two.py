# Creating a grade system using if elif else condition

score = int(input("enter your score: "))

if score >= 90:
    print("grade A")
elif score >= 80:
    print("grade B")
elif score >= 70:
    print("grade C")
elif score >= 60:
    print("grade D")
elif score >= 50:
    print("grade E")
else:
    print("you are not in qualified")


# using match & case statement
name = input("what is your name? ")

match name:
    case "ritam":
        print("burdwan")
    case "sayak":
        print("hoogly")
    case "pummy":
        print("jalpaiguri")
    case "rimu":
        print("buradwan")
    case "pradip":
        print("burdwan")
    case _:
        print("who are you?")


# try another way
name = input("what is your name? ")

match name:
    case "ritam" | "rimu" | "pradip":
        print("burdwan")
    case "sayak":
        print("hoogly")
    case "pummy":
        print("jalpaiguri")
    case "poonam":
        print("bhopal")
    case _:
        print("who are you? ")


# finding a odd number
x = int(input("what is x? "))

if x % 2 == 0:
    print("even number")
else:
    print("odd number")

# solve this problem using own function
def main():
    x = int(input("what is x? "))
    if x_even == True:
        print("even number")
    else:
        print("odd number")

def x_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# try another way
def main():
    x = int(input("what is x? "))
    if x_even(x):
        print("even")
    else:
        print("odd")

def x_even(n):
    return n % 2 == 0

main()
