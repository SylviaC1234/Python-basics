class Dog:
    def __init__(self, name, breed, hasFur):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur

    def bark(self):
        print(self.name,":woof!! Woof!!")

    def locomotive(self):
        print("Walking")

dog1 = Dog("JJ", breed="Bulldog", hasFur= True )
print(dog1.name, dog1.breed, dog1.hasFur)
dog1.bark()

dog2 = Dog("Tony", breed="German Sherpherd", hasFur = True )
print(dog2.name, dog2.breed, dog2.hasFur)

dog3 = Dog("Ann", breed="Siberian Husky", hasFur = True )
print(dog3.name, dog3.breed, dog3.hasFur)