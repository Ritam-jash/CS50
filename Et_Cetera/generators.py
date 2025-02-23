# Normal way solve this problem
def main():
    n = int(input("what's n? "))
    for i in range(n):
        print("🐏" * n)


if __name__ == "__main__":
    main()




# Solve this problem another way
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐏" * i)
    return flock


if __name__ == "__main__":
    main()








# Finaly used the generator
# Now we using the generator using yield
def main():
    n = int(input("What's n? "))
    for i in sheep(n):
        print(i)


def sheep(s):
    for i in range(s):
        yield "🐏" * i


if __name__ == "__main__":
    main()