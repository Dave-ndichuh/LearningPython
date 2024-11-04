class Rectangle:
    def shape(self):
        print("Drawing a Rectangle")

class Parallelogram:
    def shape(self):
        print("Drawing a parallelogram")

class Rhombus:
    def shape(self):
        print("Drawing a Rhombus")

r = Rectangle() #Create the object
r.shape() #Call the function

p = Parallelogram()
p.shape()

rhom = Rhombus()
rhom.shape()