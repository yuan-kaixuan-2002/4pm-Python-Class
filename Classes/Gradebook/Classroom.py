from Student import Student

class Classroom:

    def __init__(self,name):
        self.name = name
        self.students=[]

    def addStudent(self,student):
        self.students.append(student)

    def getStudent(self,name):
        for stu in self.students:
            if(stu.getName()==name):
                return stu

    def getAvg(self):
        sum = 0
        for stu in self.students:
            sum += stu.getAvg()
        return sum / len(self.students)


c1 = Classroom("Period 1")
c1.addStudent(Student("Bob"))
c1.getStudent("Bob").addGrade(91)
print(c1.getAvg())





    
