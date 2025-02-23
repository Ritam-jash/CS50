# Solve the problem to easy way
students = ["Ritam","Prdaip","Rimu",]

burdwans = []

for student in students:
    burdwans.append({"name" : student, "house" : "Burdwan"})

print(burdwans)





# Now we use the DICT COMPREHENTION
students = ["Ritam","Prdaip","Rimu",]

burdwans = {student : "Burdwan" for student in students}

print(burdwans)
