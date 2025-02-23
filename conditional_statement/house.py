# Finding name to house using if else statement
""" name = input("what's your name? ")

if name == "poonam":
    print("Bhopal")
elif name == "ritam":
    print("Bhopal")
elif name == "yin":
    print("Bhopal")
elif name == "pummy":
    print("Jalpaiguri")
elif name == "sayak":
    print("Hoogly")
else:
    print("Who are you?") """


# Finding name to house using if else statement Using match and case method
''' name = input("what's your name? ")

match name:
    case "poonam":
        print("Bhopal")
    case "ritam":
        print("Bhopal")
    case "yin":
        print("Bhopal")
    case "pummy":
        print("Jalpaiguri")
    case "sayak":
        print("Hoogly")
    case _:
        print("who are you?") '''


# Using match and case method TAW
name = input("what's your name? ")

match name:
    case "poonam" | "ritam" | "yin" :
        print("Bhopal")
    case "pummy":
        print("Jalpaiguri")
    case "sayak":
        print("Hoogly")
    case _:
        print("who are you?")
    