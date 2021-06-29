class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def addGrade(self,grade):
        self.grades.append((int)(grade))
    
    def getAvg(self):
        sum =0
        for x in self.grades:
            sum += x
        sum /= len(self.grades)
        return sum

    def getName(self):
        return self.name
