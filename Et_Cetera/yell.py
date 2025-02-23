# doing upper case
def main():
    yell("This is CS50")


def yell(words):
    print(words.upper())


if __name__ == "__main__":
    main()


# Now upper case a list use another methods
def main():
    yell(["This","is","CS50"])


def yell(words):
    upper_case = []
    for word in words:
        upper_case.append(word.upper())
    print(upper_case)


if __name__ == "__main__":
    main()


# Same problem solve into anther way using *args
def main():
    yell(["This","is","CS50"])


def yell(words):
    upper_case = []
    for word in words:
        upper_case.append(word.upper())
    print(*upper_case)


if __name__ == "__main__":
    main()


# Now solve the any number of arguments using *args
def main():
    yell("This","is","CS50")


def yell(*words):
    upper_case = []
    for word in words:
        upper_case.append(word.upper())
    print(*upper_case)


if __name__ == "__main__":
    main()


# Now we using map function solve this problem
def main():
    yell("This","is","CS50")


def yell(*words):
    upper_cased = map(str.upper, words)
    print(*upper_cased)


if __name__ == "__main__":
    main()




# Finaly we used the list comperhention
def main():
    yell("This","is","CS50")


def yell(*words):
    upper_cased = [word.upper() for word in words]
    print(*upper_cased)


if __name__ == "__main__":
    main()