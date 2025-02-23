import random
name = random.choice(["heads","tails"])
print(name)


from random import randint
name= randint(1,100)
print(name)


from random import shuffle
name = ["poonam","pummy","ritam","sayak"]
shuffle(name)
for names in name:
    print(names)


from statistics import mean
num = mean([100,90])
print(num)

