
'''
if temperature is greater than 30
    it's a hot day
otherwise if it's less than 10 
    it's cold day 
otherwise
    it's neither hot nor cold

'''

temprature = 9

if temprature > 30:
    print("It's hot day")
    
elif temprature <10:
    print("It's cold day")
    
else:
    print("It's neither hot nor cold day")
    

'''
# Exercise

if name is less than 3 characters long 
    name must be at least 3 characters 
otherwise if it's more than 10 characters 
    name can be a maximum 10 characters 
otherwise 
    name looks good!
'''    


name = 'M'

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 10 :
    print("name can be a maximum of 10 characters")
    
else:
    print("name looks good!")