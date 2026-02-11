#Polymorphism is the many forms a method can have

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

class Rhombus:
    def draw(self):
        print("Drawing a rhombus")

class Parallelogram:
    def draw(self):
        print("Drawing a parallelogram")

R = Rectangle()
R.draw()

Rh = Rhombus()
Rh.draw()

P = Parallelogram()
P.draw()