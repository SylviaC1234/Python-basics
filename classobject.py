#Class is a blueprint of an object
#Object is an instance of a class
class Employee:
    # Attributes/Variables
    name = "James"
    age = 45
    gender = "Male"
    salary = 70000.00

    #Behaviour/Functions
    def eat(self):
        print("Employee eats")

employee1 = Employee() #creating an object
print(employee1.name)



employee2 = Employee()
employee3 = Employee()
