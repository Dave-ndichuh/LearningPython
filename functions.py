#Function- A block of code that allows you to perform a task or an action
#Built-in Library Functions
y = max(56,78,98,23,12)
print("The maximum value is:",y)

x = min(67, 10, 45, 32, 67)
print("The minimum value is:",x)

z = pow(2,3)
print("The power value is:",z)

#User-defined Functions
def greeting(): #defining the function
    print("Hello there!")
greeting() #Calling the function


def multiply():
    num1 = 23
    num2 = 10
    print("The product value of the two numbers is:",num1*num2)
multiply()

#Parameters and Arguments
#A parameter is a variable used to store values
#Arguments are the values
def add(a, b):
    print("The sum is:", a+b)
add(3,6)
add(2,2)

#to display employee details
def employee(fullname,age,position,marital_status):
    print("Name:",fullname, "Age:", age, "Position:",position, "Marital Status:",marital_status)
employee("Mark Joe", 45,"CEO","married")
employee("Jane Esther", 30,"HR","single")
employee("Din Plit", 24,"Clerk","married")




