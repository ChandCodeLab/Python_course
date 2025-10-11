names =['Jhon','Bob','Ram','Manoj']
print(names[-2])  #second items for the last --> Ram
print(names[0])
print(names[3])
# Print the list with range
print(names[1:])
print(names[:3])
print(names[1:3])
print(names) #before assign

# assign the new elements to the lists
names[0]='Hari'
print(names)


#WAP to find the largest number in a list.

numbers =[122,6,5,10,12]
max = numbers[0]
for number in numbers:
    if number>max:
        max=number
print(f'The largest number is: {max}')

