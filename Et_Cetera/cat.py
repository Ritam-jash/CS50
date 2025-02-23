class Cat:
    MEOWS = 3


    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meows")


cat = Cat()
cat.meow()