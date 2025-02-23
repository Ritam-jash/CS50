# Exception_handling
def main():
    x = get_number()
    print(f"x is {x}")


def get_number():
    while True:
        try:
            x = int(input("what is x? "))
        except ValueError:
            print("X is not a int")
        else:
            return x


if __name__ == "__main__":
    main()


# Now we introduce pass keyword
def main():
    x = get_number()
    print(f"x is {x}")


def get_number():
    while True:
        try:
            x = int(input("what is x? "))
            return x
        except ValueError:
            pass


if __name__ == "__main__":
    main()




# now we introduce prompt keyword
def main():
    x = get_number("what is x? ")
    print(f"x is {x}")


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


if __name__ == "__main__":
    main()
        






# Libraries
import random

coin = random.choice(["heads", "tails"])
print(coin)




# taw
from random import choice

coin = choice(["heads", "tails"])
print(coin)




import random
num = random.randint(1, 100)
print(num)




# cards shuffle
import random

cards = ["king", "queen", "tekka", "saheb"]
random.shuffle(cards)

for card in cards:
    print(card)




# now using statices laibraries
import statistics

num = statistics.mean([100, 90])

print(num)


# Taw
from statistics import mean

num = mean([100, 90])
print(num)