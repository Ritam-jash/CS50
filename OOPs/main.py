# # Learn Basic Tuple, Dict using function
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()




# # TAW put the value into a tuple
# def main():
#     name , house = student()
#     print(f"{name} from {house}")


# def student():
#     name = input("Name: ")
#     house = input("house: ")
#     return (name , house)


# if __name__ == "__main__":
#     main()




# # TAW put the value into a tuple
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("house: ")
#     return (name , house)


# if __name__ == "__main__":
#     main()




# # TAW put the value into a tuple [Tuple is a imutible data type] HERE IS A EXAMPLE: 
# def main():
#     student = get_student()
#     if student[0] == "Sayak":
#         student[1] = "Hoogly" # show me the TypeError: 
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("house: ")
#     return (name , house)


# if __name__ == "__main__":
#     main()






# # TAW now put the value into a dict
# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()



# # TAW now put the value into a dict [Dict is a mutible data type] HERE IS A EXAMPLE: 
# def main():
#     student = get_student()
#     if student["name"] == "Sayak":
#         student["house"] = "Hoogly"
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()






# # now we create a classes
# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()




# # taw show me this error:- TypeError: Student() takes no arguments
# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student


# if __name__ == "__main__":
#     main()




# # NOW SOLVE THIS ERROR  using __init__ method:
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student


# if __name__ == "__main__":
#     main()




# # If user does't put the value that case memory will be ocopai so that's time how can we handel it
# # If user input does't matched that case show this error
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in["Burdwan","Westbengal","India"]:
#             raise ValueError("House not matched")
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student


# if __name__ == "__main__":
#     main()




# Now we learn dender str method ()
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Burdwan", "Westbengal", "India"]:
            raise ValueError("House not matched")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("Hosue: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
