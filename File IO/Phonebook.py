book = []

db = open("db.txt",'r')

for line in db.readlines():
    line = line.strip()
    person = line.split(",")
    book.append(person)

db.close()

while(True):
    mode = input("Press 1 to add, 2 to retrieve, 3 to quit:")

    if(mode == "1"):
        name = input("Enter the name:")
        num = input("Enter the number:")
        person = [name,num]
        book.append(person)

    elif(mode == "2"):
        name = input("Enter the name:")
        for person in book:
            if(person[0]== name):
                print(person[1])

    elif(mode == "3"):

        db = open("db.txt","w")
        for person in book:
            db.write(person[0]+","+person[1]+"\n")

        db.close()
        break
            
