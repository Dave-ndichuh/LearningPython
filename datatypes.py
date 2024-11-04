#Data type: used to classify values (int, float, string, char, boolean)
number = 25 #this is an integer (Int)
second = 56.78 #this is a float (Float)
text = "Hello there" #this is a string (String- Str)
isPythonInteresting = True #this is a Boolean (Bool)

#Data Structures in Python: Multiple values stored in a single variable
#1- lists
cars = ["toyota", "mercedes", "nissan", "vw"] #this is a list and the values/elements are ordered and changeable

#2- tuples
fruits = ("apple", "pear", "orange", "grape") #this is a Tuple and the values/elements are ordered but unchangeable

#3- sets
countries = {"Kenya", "Tunisia", "Algeria"} #this is a set and the elements are unordered and unchangeable/immutable

#4- dictionary
student = {
    "first_name": "John", #first_name- key, John- value
    "last_name": "Doe",
    "age": 34,
    "course": "Web development",
    "nationality": "India"
} #this is a Dictionary- it has a key and a value pair


print(number)
print(second)
print(text)
print(isPythonInteresting)

#determining datatype
print(type(number))
print(type(second))
print(type(text))
print(type(isPythonInteresting))
print(type(student))
print(type(countries))

#printing the data structures
print(cars)
print(fruits)
print(countries)
print(student)
print(student["first_name"]) #print a specific value in a dictionary

#Typecasting- the process of converting from one datatype to another
print(float(number))
print(int(second))
