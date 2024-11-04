class Student:
    #the following are properties/characteristics/attributes
    name = "Joe"
    age = 21

    #the following are behaviors/methods/functions
    def study(self):
        print("Student is Studying")

student1 = Student()  #Instantiating/Creating an object
student1.study()

print(student1.name, student1.age)