# using RANDOM libraries
''' import random
name = random.choice(["heads","tails"])
print(name) '''

#TAW
''' from random import choice
name = choice(["one","two"])
print(name) '''

#TAW
import random
num = random.randint(1, 100)
print(num)

#TAW
cards = ["jack","king","queen"]
random.shuffle(cards)
for card in cards:
    print(card)

# Another libraries
import statistics
print(statistics.mean([100, 90]))
