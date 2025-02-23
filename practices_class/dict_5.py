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




# CREAT A BRICK GAME
def main():
    number = get_num()
    print_squar(number)

def get_num():
    n = int(input("enter your number: "))
    return n

def print_squar(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()
