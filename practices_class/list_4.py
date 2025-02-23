# acess a list using for loop
students = ["ritam","rimu","pradip","sayak"]

for student in students:
    print(student)


# TAW
students = ["ritam","rimu","pradip","sayak"]

for i in range(len(students)):
    print(students[i])

# TAW
students = ["ritam","rimu","pradip","sayak"]

for i in range(len(students)):
    print(i+1, students[i])


# CREATING A DICTINARY
students = {
    "Ritam" : "Burdwan",
    "Rimu" : "Burdwan",
    "Pradip" : "Burdwan",
    "Sayak" : "Hoogly",
    "Pummy" : "Jalpaiguri"
}

for student in students:
    print(student, students[student], sep=", ")
