

# Define a class
class Dog:
    sound = "Bark"  #class attribute
    
    
    # Object
dog1 =Dog()  #creating object from class
print(dog1.sound)  #Accessing the class


# The __init__() Method

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age =age
        
p1 = Person("Manoj", 23)

print(p1.name)
print(p1.age)
         
# The __str__() Method

class Person2:
    def __init__(self,name,age):
        self.name =name
        self.age =age
        
    def __str__(self):
        return f" Name : {self.name } & Age : {self.age} yrs"

p2 =Person2("Manoj Chand" ,24)

print(p2)

# Create Methods

class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age =age
        self.gender = gender
    
    def function(self):
        print("Hello my name is " ,self.name)
        
s1= Student("Rajan",12,"male")
s1.function()