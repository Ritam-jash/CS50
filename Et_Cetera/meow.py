def mewo(n: int):
    for _ in range(n):
        print("Meow")


number: int = int(input("Number: "))
mewo(number)


# try another way solve this problem
def mew(n: int) -> None:
    for _ in range(n):
        print("Meow")


number: int = int(input("Number: "))
mews: str = mew(number)

print(mews)


# Now solve this problem to None
def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("number: "))
mews: str = meow(number)
print(mews, end="")