# find the unique house from the dict
students = [
    {"name" : "Ritam", "house" : "Burdwan"},
    {"name" : "Sayak", "house" : "Hoogly"},
    {"name" : "Rimu", "house" : "Burdwan"},
    {"name" : "Pradip", "house" : "Burdwan"},
    {"name" : "Poonam", "house" : "Bhoopal"}
]

houses = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])


for house in sorted(houses):
    print(house)


# Try another way to solve this problem using set
students = [
    {"name" : "Ritam", "house" : "Burdwan"},
    {"name" : "Sayak", "house" : "Hoogly"},
    {"name" : "Rimu", "house" : "Burdwan"},
    {"name" : "Pradip", "house" : "Burdwan"},
    {"name" : "Poonam", "house" : "Bhoopal"}
]


houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)