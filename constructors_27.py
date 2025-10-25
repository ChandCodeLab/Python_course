# Constructors in python
class Dog:
    species = "canine" #class attribute
     
    def __init__(self,name,age):
        self.name = name    #Instance attribute 
        self.age=age   #Instance attribute 
    
    
# Creating an object of the Dog class
dog1 =Dog("Jack",3)

print(dog1.name)
print(dog1.species)
print(dog1.age)



class Person:
        
    def __init__(self,name):
        self.name = name 
        
    def talk(self):
        print(f"Hi, I am {self.name}")
        
        
person1 = Person("Manoj Chand")
print(person1.name)
person1.talk()

person2 =Person("Rakesh Singh")
person2.talk()
        
        
# __str__() Method

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
dog2 =Dog("jolly",4)
dog3 = Dog("Charlie",6)

print(dog2)
print(dog3)
        