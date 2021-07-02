from Student import Student
from Classroom import Classroom

classrooms = []


def classTasks(selected):
    while(True):
        mode2 = ("Enter 1 to add student, 2 to select students, 3 to quit")
        if(mode2 == "1"):
            name = input("Enter a name")
        break




while(True):
    mode1 = input("Enter 1 to create class, enter 2 to select class, 3 to quit")
    print("List of classes:")
    for c in classrooms:
        print(c.getName())

    if(mode1 == "1"):
        temp = input("Enter the name of the class")
        classrooms.append(Classroom(temp))
    elif(mode1 == "2"):
        temp = input("Enter the name of the class")
        for c in classrooms:
            if(c.getName()== temp):
                classTasks(c)
