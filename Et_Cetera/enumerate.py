# Counting the number of list
students = ["Ritam", "Pradip", "Rimu"]

for i in range(len(students)):
    print(i+1, students[i])




# Now we using the enumerate function solve this same problem
students = ["Ritam", "Pradip", "Rimu"]

for i, student in enumerate(students):
    print(i+1, student)