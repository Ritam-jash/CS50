# acces a dict in for loop
friends = {
    "pummy":"jalpaiguri",
    "sayak" : "hogli",
    "punom" : "bhopal",
    "ritam" : "burdwan"
}

# print(type(friend))

for friend in friends:
    print(friend,friends[friend], sep= "  ")

# print(type())



# handeling big dict into a list
peoples = [
    {"name" : "ritam", "location" : "burdwan", "age" : 23},
    {"name" : "sayak", "location": "hogli", "age" : 19},
    {"name" : "pummy", "location" : "jalpaiguri", "age" : 20},
    {"name": "poonam", "location" :"bhopal" , "age" : 24}
]


for people in peoples:
    print(people["name"], people["location"], people["age"], sep="    ")


# next question
# creat a function 3 * 3
def main():
    print_squar(3)


def print_squar(size):
    # for each row in squar
    for i in range(size):
        # for each coloum in squar
        for j in range(size):
            # print squar
            print("#", end="")
        print()

main()


# try another way
def main():
    print_squar(3)

def print_squar(size):
    for i in range(size):
        print("*" * 3)

main()