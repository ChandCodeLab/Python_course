# functions in python 
def greet_user():
    print("Hi there !")
    print("Welcome to Nepal")
    
    
print("start")
greet_user()
print("finish")

# WAP to check weather the number is odd or een 

def even_odd(x):
    if (x%2== 0):
        return "This is a even number"
    else:
        return "This is a odd number"


print(even_odd(16))
print(even_odd(17))


# Types of Function Arguments

# 1 default arguments
def my_fun(x, y=40):
    print("x :",x)
    print("y :",y)
    
my_fun(10)
my_fun(22,44)

# 2. Keyword Arguments

def student(fname, lname):
    print(fname,lname)


student("Manoj","Chand")
student(lname="Singh",fname= "Shital")

# 3. Positional Arguments

def name_age(name, age):
    print("Hi, I am ", name)
    print("My age is ",age)
# case-1
name_age("Suraj",27)

# case-2
name_age(27,"Suraj")


# 4. Arbitrary Arguments
'''
*args in python (Non-keyword Arguments)
**kwargs in python (keyword Arguments)
'''
def my_fun(*args,**kwargs):
    print("Non-keyword Arguments(*args)")
    for arg in args:
        print(arg)
        
    print("Keyword Arguments (**kwargs)")
    for key,vlaue in kwargs.items():
        print(f"{key}=={vlaue}")
        
# Function call with both types of arguments
my_fun('Hey', 'Welcome', first='to ', mid='to', last='Nepal')        


# Function within Functions
def f1():
    s="I am Python Developer"
    def f2():
        print(s)
    f2()
f1()
     


# Anonymous Functions

def cube(x): return x*x*x  #without lambda
cube_l = lambda x : x*x*x   #with lambda

print(cube(7))
print(cube_l(7))



# Return Statement in Function

def square_value(num):
    '''This function returns the square 
    value of the entered number
    
    '''
    return num**2

print(square_value(2))
print(square_value(-5))
 
# Pass by Reference and Pass by Value
'''
Mutable objects
Immutable objects
'''
#Function modifies the first element of list 

def my_function(x):
    x[0]=20
    
lst = [10,11,12,13]
my_function(lst)
print(lst)     #list is modified

# Function tries to modify an integer
def my_function(x):
    x = 20
    
    
a =10 
my_function(a)
print(a)        #integer is not modified


# Recursive Functions
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("The fact is :",factorial(4))