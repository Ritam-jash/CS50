# file i/o
name = input("enter your name? ")
# now we open the name.txt file
file = open("name.txt","w")
# now we write the name in file
file.write(name)
# now we close the file
file.close()

# But there show a problem that is when i input the new name then old name automaticly remove
# Now we solve this problem using append method
name = input("what is your name? ")
file = open("name.txt","a")
file.write(name)
file.close()


# But there show me another problem that is when i input the name then it will be automaticly attached all name (like:- ritamsayak)
# Now we solve this problem using \n
name = input("what is your name ? ")
file = open("name.txt","a")
file.write(f"{name}\n")
file.close()


# Now we solve this problem using with keyword & shortest way solve this problem
name = input("what is your name ? ")
with open("name.txt","a") as file:
    file.write(f"{name}\n")


# now we open the file
with open("name.txt","r") as file:
    lines = file.readlines()

for line in lines:
    # print("hello,", line,end="")
    print("hello,",line.rstrip())


# TAW
with open("name.txt","r") as file:
    for line in file:
        print("hello,",line.rstrip())


# Now we sorted the list
names = []

with open ("name.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")