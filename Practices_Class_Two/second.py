score = int(input("what is you score? "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 50:
    print("E")
else:
    print("Not find your marks")




name = input("enter your name? ").title()

match name:
    case "Ritam" | "Pradip" | "Rimu":
        print("Burdwan")
    case "Sayak":
        print("Hoogly")
    case "Poonam":
        print("Bhoopal")
    case "Pummy":
        print("Jalpaiguri")
    case _:
        print("Not mtached")




def main():
    x = int(input("enter the x? "))
    if even(x):
        print("Even")
    else:
        print("odd")


def even(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()