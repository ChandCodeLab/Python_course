coordinates = (1,2,3)
# x =coordinates[0]
# y =coordinates[1]
# z=coordinates[2]

x,y,z =coordinates
print(x)
print(y)
print(z)

# Using _ for Unused Values
a, _, c = (100, 200, 300)
print(a)  
print(c)

# Using * for Variable-Length Unpacking

a, *b =(1,2,3,4,6,8)
print(a)
print(b)                    

# Tuple Unpacking with * in Function Arguments

def add(*args):
    return sum(args)

print('The total sum is :',add(1,4,3,5,3))

# Using * for Argument Unpacking: Tuple unpacking can also be used when calling a function

def add(a,b,c):
    return a+b+c

nums = (1,2,3)
print(add(*nums))