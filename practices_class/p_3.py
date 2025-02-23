# loop
i = 3
while i != 0:
    i -= 1
    print(i)

#Taw
i = 0
while i < 3:
    print(i)
    i += 1


# using function
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()


#TAW
def main():
    number = get_number()
    mew(number)


def get_number():
    while True:
        n = int(input("what is n? "))
        if n > 0:
            break
    return n


def mew(n):
    for _ in range(n):
        print("meaw")

main()


# creating a loop
while True:
    n = int(input("enter the num: "))
    if n > 0:
        break

for i in range(n):
    print("Meaw")


# TAW using own function
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("enter the number: "))
        if n > 0:
            return n


def meow(n):
    for i in range(n):
        print(i,"Meow")

main()