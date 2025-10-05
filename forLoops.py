# String
for item in 'python':
    print(item)
    
# list 
for item in ['Ram','Sagar','Saksham','Manoj','Shital']:
    print("My name is",item)
    

for item in [1,2,3,4,5,6,7]:
    print(item)

# range function
for item in range(10):
    print(item)
    
# range(initial, final)
for item in range(5,9):
    print(item)

# range(initial,final,step/gap)
for item in range(2,20,4):   
    print(item)



#To calculate the total cost of all the items in a shopping cart.
prices = [10,20,30,40]
total = 0
for price in prices:
    total += price
print(f"Total:{total}")