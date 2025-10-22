'''
try 
    # code 
except SomeException:
    # code
else:
    # code 
finally:
    # code
'''
try:
    age =int(input('Age :'))
    print(age)   
except ValueError:
    print("Invalid Value")
    

# Example
try:
    n=0
    res = 100/n
except ZeroDivisionError:
    print("Can't be divided by zero!")
    
except ValueError:
    print("Enter a valid number ")
    
else:
    print("Result is :", res)
    
finally:
    print("Exception complete.")


# raise expection type
def set(age):
    if age<0:
        raise ValueError("Age cannot be negative.")
    print(f'Age set to {age}')

try:
    set(5)
    
except ValueError as e:
    print(e)
    
