# Now we learn about csv module (reader) to read the all csv file
"""
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name" : name, "house" : house})

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")
"""


# Now we use csv Dictreader ,which will be iterate over the file top to bottom 
# [loading in each line of text not as a list of columns BUT as a dictionary of column]
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name" : row['name'], "house" : row['house']})


for student in sorted(students, key=lambda student : student["name"]):
    print(f"{student['name']} is from {student['house']}")