class Student:
    def __init__(self,name,course,age,feesPaid):
        self.name = name
        self.course = course
        self.age = age
        self.fees = feesPaid

    def printStudent(self):
        print("name:",self.name,"course:",self.course,"age:",self.age,"feesPaid",self.fees)

Student1 = Student("Jessy Jane", "Data Science", 29,True)
print(Student1.name,Student1.course,Student1.age,Student1.fees)

Student2 = Student("John Hunter", "MIT", 28,False)
print(Student2.name,Student2.course,Student2.age,Student2.fees)

Student3 = Student("Maria Ann", "Cyber Security", 25,True)
print(Student3.name,Student3.course,Student3.age,Student3.fees)
