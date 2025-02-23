# we use writer function in store the data into list
""" import csv

name = input("what's your name? ")
house = input("where's your house? ")

with open("friends.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house]) """


# Now we store the data in dictionary
import csv

name = input("what's your name? ")
house = input("where's your house? ")

with open("friends.csv", "a") as file:
    writer = csv.DictReader(file, fieldnames=["name", "house"])
    writer.writerow({"name" : name, "house" : house}) # error last line
