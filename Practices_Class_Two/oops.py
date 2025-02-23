# getter & setter
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return(f"{self.name} from {self.house}")


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Burdwan", "India", "WB"]:
            raise ValueError("House not matched")
        self._house = house

    
def main():
    student = get_name()
    print(student)


def get_name():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()








# Inheritance
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Ritam", "Burdwan")

professor = Professor("Devid Melon", "CSE")

print(f"{student.name} from {student.house}")

print(f"{professor.name} teach us {professor.subject}")








# operator overloading
class Vault:
    def __init__(self, cash=0, gold=0, coin=0):
        self.cash = cash
        self.gold = gold
        self.coin = coin

    def __str__(self):
        return f"{self.cash} cash, {self.gold} gold, {self.coin} coin"

    
    def __add__(self, other):
        case = self.cash + other.cash
        gold = self.gold + other.gold
        coin = self.coin + other.coin
        return Vault(case,gold,coin)

    
ritam = Vault(100, 50, 200)
print(ritam)
sayak = Vault(150, 100, 200)
print(sayak)
total = ritam + sayak
print(total)








# class_method
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in["India", "Westbengal", "India"]:
            raise ValueError("House not in matched")
        self._house = house

    
    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()