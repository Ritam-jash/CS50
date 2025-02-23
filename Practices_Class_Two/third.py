# LOOP & DICT & LIST
i = 3
while i != 0:
    i -= 1
    print(i)

i = 0
while i < 10:
    i += 1
    print(i)


# using function
def main():
    meow(3)


def meow(n):
    for _ in range(n):
        print("Meow")


if __name__=="__main__":
    main()


# TAW using own function
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("enter your num? "))
        if n > 0:
            return n
        

def meow(n):
    for i in range(n):
        print(i+1, "Meow")


if __name__ == "__main__":
    main()




# acess alist using loop
students = ["ritam", "sayak", "pradip", "rime", "pummy"]

for student in students:
    print(student)

# Taw
students = ["ritam", "sayak", "pradip", "rime", "pummy"]

for i in range(len(students)):
    print(students[i])


# TAW
students = ["ritam", "sayak", "pradip", "rime", "pummy"]

for i in range(len(students)):
    print(i+1, students[i])

# Creating a dict
students = {
    "name" : "ritam",
    "branch" : "ECE",
    "location" : "Burdwan",
    "state" : "WB"
}

for student in students:
    print(student, students[student], sep=", ")




# create a big dict in list and acess it
students = [
    {"name" : "ritam", "place" : "burdwan", "age" : 24},
    {"name" : "rimu", "place" : "burdwan", "age" : 23},
    {"name" : "pradip", "place" : "burdwan", "age" : 23},
    {"name" : "sayak", "place" : "hoogly", "age" : 19},
    {"name" :"pummy", "place" : "jalpaiguri", "age" : 20}
]


for student in students:
    print(student["name"], student["place"], student["age"], sep=", ")


# Create a brick game
def main():
    number = get_num()
    print_squar(number)


def get_num():
    n = int(input("enter your num? "))
    return n


def print_squar(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    main()



# searching a list

names = ["ritam", "sayak", "pradip", "rimu", "pummy"]

for i in range(len(names)):
    if names[i] == "pummy":
        print(i, names[i])