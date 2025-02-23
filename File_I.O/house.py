# # we acess the all data and separet via .split(",")
# with open("house.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")


# # Now we sorted the data in empty list
# students = []

# with open("house.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)


# # now we store the data inside of dict
# students = []

# with open ("house.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")


# # now we solve the problem in another way
# students = []

# with open ("house.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name, "house" : house}
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")


# # now we shorted the data inside of dict in empty list
# students = []

# with open ("house.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name, "house" : house}
#         students.append(student)


# def get_name(student):
#     return student["name"]


# for student in sorted(students, key= get_name):
#     print(f"{student['name']} is in {student['house']}")



# now we collect data from one file and store it dict and then sorted into list
""" students = []

with open("house.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {"name" : name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}") """

# # TAW
# students = []

# with open("house.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name, "house" : house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")


# TAW BT NOW WE USING A lamda FUNCTION THAT'S CALLLED NULL FUNCTION
students = []

with open("house.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
