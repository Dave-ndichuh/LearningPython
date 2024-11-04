class Person:
    def __init__(self,name,age,gender,height,weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def movement(self):
        print("Person is walking")

a = Person("Joe", 34, "Male", 6, 70)
print(a.name, a.age, a.gender, a.height, a.weight)
b = Person("Mary", 30, "Female", 5.5, 67)
print(b.name, b.age, b.gender, b.height, b.weight)
c = Person("John", 25, "Male", 6, 50)
print(c.name, c.age, c.gender, c.height, c.weight)

