customer = {
    'name':'Manoj',
    'age':25,
    'is_verified':True
    
}
print(customer)

# update the value
customer['name']='Sagar'

print(customer['name'])
print(customer.get('age'))
print(customer.get('birthdate','Nov 11 2001'))


# Dictionary can be created by placing a sequence of elements within curly {} braces, separated by a 'comma'. 
d1 = {1 :"Hello",2:"World"}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a ="Hello",b="World")
print(d2)


# Accessing Dictionary Items
d = {'name':"Hari",1:"Python",(1,2):[1,2,4]}

# Access using key
print(d['name'])

# Access using get()
print(d.get('name'))




#Adding a new key-value pair
d["age"]=22

# Updating an existing value
d[1]="Python dict"

print(d)

# Removing Dictionary Items

dict ={
    1:"Geeks",2:"For",3:"Geeks",'age':25
}

# Using del to remove an item 
del dict["age"]
print(dict)

# Using pop() to remove a item and return the value
val = dict.pop(1)
print(val)
print(dict)

# using popitem to removes and returns
# the last key-value pair.
key, val = dict.popitem()
print(f"key:{key},value:{val}")
print(dict)

# clear all items from the dictionary
dict.clear()
print(dict)


# Iterating Through a Dictionary

di ={1:'Me',2:"Nepali","age":24}

# Iterate over keys
for key in di:
    print(key)
    
# Iterate over values
for value in di.values():
    print(value)
    
# Iterate over key-value pairs
for key, value in di.items():
    print(f"{key}:{value}")
    
    
    
# Nested Dictionaries
dictionaries= {
    "name":"Manoj Chand",
    "birthdate" :"NOv 11 2001",
    "address":{
        "muncapality":"Malikarjun",
        "ward .no":6,
        "district":"Darchula"
    }
}

print(dictionaries)


# Problem-convert the numbers into words 

phone=input("Phone")
digits_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output = ''
for ch in phone:
    output+=digits_mapping.get(ch, "!") + " "
print(output)


