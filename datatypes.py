age = 18 #Integer
length = 45.6 #Float
greeting = "Hello there" #String
hasFeathers = True #Boolean


#Data structures-multiple values stored in one variable
fruits = ["Banana", "Mango", "Pineapple"] #List-Ordered and changeable, different datatypes
courses = ["MIT", "DataScience", "CyberSecurity"] #Array-Like list but carries similar datatypes
cars = ("Mercedes", "Ford", "Nissan", "Ferrari") #Tuple-Ordered and unchangeable
countries = {"Zambia", "Canada", "India", "Spain"} #Set-Unordered and unchangeable
student = {"name" : "Sylvia",
           "course" :"MIT" ,
           "age" : 18,
           "nationality" :"Kenyan" ,
           "gender" :"female"} #Dictionary-Key value pair




print(age)
print("The length is", length)
print(fruits)
print(countries)
print(student["name"])


#TypeCasting-Converting one datatype to another
print(float(age))
print(int(length))
