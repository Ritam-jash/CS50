''' def main():
    spacecraft= {"name": "voyager 1", "distance": 163}
    print(creat_report(spacecraft))


def creat_report(spacecraft):
    return f"""
    ======= REPORT ======

    name: TODO
    destance: TODO

    =====================
    """
main() '''


# TAW acess the dict 
''' def main():
    spacecraft = {"name": "voyager 1", "distance": 163}
    print(creat_report(spacecraft))


def creat_report(spacecraft):
    return f"""
    ===== REPORT ====
    name: {spacecraft["name"]}
    distance : {spacecraft["distance"]}
    time : {spacecraft.get("time", "Unknown")} #if keys don't exist then we using .get method
    =================
    """
main() '''


# TAW update the dictinary
''' def main():
    student = {"name":"pummy","age": 19}
    student.update({"location":"jalpaiguri","class": "2nd year"})
    print(creat_report(student))

def creat_report(student):
    return f"""
    ===== REPORT ====
    Name : {student.get("name","Unknown")}
    Age : {student.get("age", "Unknown")}
    Location : {student.get("location","Unknown")}
    Class : {student.get("class","Unknown")}
    Hobby : {student.get("hobby","Unknown")}

    ================================================
    """
main() '''


# TAW using for loop acess the keys and values
''' employer = {
    "name" : "punoom",
    "company" : "TCS",
    "qualification" : "MCA",
    "age" : 24,
    "location" : "bhopal"
}

for name in employer.keys():
    print(f"{name}: {employer[name]}") '''


# TAW convert au to mitter
distances = {
    "voyager 1": 163,
    "voyager 2": 136,
    "pioneer 10": 80,
    "new horizons": 58,
    "pioneer 11": 44
}
def main():
    for distance in distances.values():
        print(f"{distance} AU is {converter(distance)} m")


def converter(au):
    return au * 149597870700
main()