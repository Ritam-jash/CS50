""" x = int(input("what is x? "))
y = int(input("what is y? "))

if x < y:
    print("x is less then y")
elif x > y:
    print("x is greater then y")
else:
    print("x is equal to y") """


''' a = int(input("what is a? "))
b = int(input("what is b? "))

if a > b or a < b:
    print("a is not equal to b")
else:
    print("a is equal to b")


# try another way
a = int(input("what is a? "))
b = int(input("what is b? "))

if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")


# try another way
a = int(input("what is a? "))
b = int(input("what is b? "))

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b") '''


# score board
""" score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Geade: A")
elif score >= 80 and score <= 89:
    print("Grade: B")
elif score >= 70 and score <=79:
    print("Grade: C")
elif score >= 60 and score <= 69:
    print("grade: D")
elif score >= 50 and score <= 59:
    print("Grade: E")
else:
    print("Grade: F") """


# Try another way
""" score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Geade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("grade: D")
elif score >= 50 and score < 60:
    print("Grade: E")
else:
    print("Grade: F") """


# Try to best way
''' score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F") '''


# Shortest way to creat same problem
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")