def view_all():
    talaba = {}
    try:
        with open('stundent.txt', 'r') as f:
            data = f.readlines()
            for user in data:
                id, name, num = user.strip().split()
                talaba[int(id)] = {'name': name, 'num': num}
    except FileNotFoundError:
        print('File not found!')
    return talaba


def subject():
    update = {}
    try:
        with open('update.txt', 'r') as fl:
            data = fl.readlines()
            for up in data:
                id, name = up.strip().split()
                update[int(id)] = name
    except FileNotFoundError:
        print("File not found!")
    return update


def royhat_malumot():
    grade = []
    try:
        with open('grades.txt', 'r') as file:
            data = file.readlines()
            for gred in data:
                grade.append(gred.strip())
    except FileNotFoundError:
        print("File not found!")
    return grade


def talabaqosh(id, name, num):
    try:
        with open('students.txt', 'a') as fil:
            fil.write(f"{id}\t{name}\t{num}\n")
        print("Student successfully added!")
    except FileNotFoundError:
        print('File not found!')


def fanqoshish(id, name):
    try:
        with open('update.txt', 'a') as file:
            file.write(f"{id}\t{name}\n")
        print("Subject successfully added!")
    except FileNotFoundError:
        print("File not found!")

while True:
    print("1. All\n2. Subject\n3. Grades\n4. Add student\n5. Add Subject")
    txt = input("Select an option: ")
    if txt == '1':
        print(view_all())
    elif txt == '2':
        print(subject())
    elif txt == '3':
        print(royhat_malumot())
    elif txt == '4':
        name = input("Name: ")
        num = int(input("Num: "))
        id = int(input("ID: "))
        talabaqosh(id, name, num)

    elif txt == '5':
        id = int(input("ID: "))
        name = input("Name: ")
        fanqoshish(id, name)
