#Functions/Methods -It is a block of code use to perform a task
# used to hold a code that does a specific task. The code could be run multiple
# times within the program

#Standard library/Inbuilt functions - Already exist
y = max(56, 67, 345, 213, 5666, 6788, 2344)
print(y)

x = min(56,897, 76, 897, 98)
print(x)



#User defined functions - Created by the user
def school():
    print("Emobilis")
school()


def multiply():
    print(15 * 5)
multiply()

#parameters/variables
#Arguements/Values
def product(x, y):
    print(x * y)
product(6, 10)
product(45, 62)


def students(name, age, gender):
    print(name, age, gender)
students("lewis", 19, "male")
students("Christian", 18, "male")
students("Jane", 19, "female")

#python program to display details of 5 employees at Emobilis
#Use a user-defined function with the help of parameters and arguments
#Details - Fullname, position, age, gender


def employees(name, position, age, gender):
    print(name, position, age, gender)
employees("Paul Mwangi,", "Managing director,", "40,", "male")
employees("Grace Akinyi,", "secretary,", "27,", "female")
employees("Jessica Hunter,", "lecturer,", "38,", "female")
employees("william Baker,", "lecturer,", "29,", "male")
employees("Eloise Sang',", "lecturer,", "32,", "female")
    




