# students = [
#     {"name" : "Ritam", "house" : "Burdwan"},
#     {"name" : "Sayak", "house" : "Hoogly"},
#     {"name" : "Rimu", "house" : "Burdwan"},
#     {"name" : "Pradip", "house" : "Burdwan"},
#     {"name" : "Poonam", "house" : "Bhoopal"}
# ]


# burdwans = [
#     student["name"] for student in students if student["house"] == "Burdwan"
# ]

# for burdwan in sorted(burdwans):
#     print(burdwan)




# Now we solve this problem another way using FILTER and sorted it
students = [
    {"name" : "Ritam", "house" : "Burdwan"},
    {"name" : "Sayak", "house" : "Hoogly"},
    {"name" : "Rimu", "house" : "Burdwan"},
    {"name" : "Pradip", "house" : "Burdwan"},
    {"name" : "Poonam", "house" : "Bhoopal"}
]


def is_burdwans(s):
    return s["house"] == "Burdwan"


burdwans = filter(is_burdwans, students)

for burdwan in sorted(burdwans, key=lambda s: s["name"]):
    print(burdwan["name"])
