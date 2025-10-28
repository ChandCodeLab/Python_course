class Animal:
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print("Animal name :", self.name)
         
class Dog(Animal):
    def sound(self):
        (self.name, "Barks")
        
        
d=Dog("Monny")
d.info()
d.sound()


# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname =lname
        
    def printname(self):
        print(f'Fullname : {self.fname} {self.lname}')

#Use the Person class to create an object, and then execute the printname method:
x =Person("Manoj","Chand")
x.printname()

# Use the Student class to create an object, and then execute the printname method  which will inherit the printname method form the Person class

class Student(Person):
    pass

x=Student("Mike","Tike")
x.printname()