# list methods or functions


num = [3,3,2,42,4,3,6,5,3,8]

# to insert the number in the last of the list
num.append(20)
print(num)

# to inster the number in the first of the list
num.insert(0,1)  #num.insert(index,item)
print(num)

# To remove the element from the list
num.remove(5)
print(num)

# # remove all the elements from the list
# num.clear()
# print(num)

# remove the last item in the list
num.pop()
print(num)

# existence of the items in the list 
print(num.index(42))

print(42 in num)
print(402 in num)

# count the numbers of the same items in the list
print(num.count(3))

# to sort the list in ascending order
num.sort()
print(num)

# to sort the list in descending order   
num.sort()
num.reverse()
print(num)

# copy the origional list 
print("The origional list is ",num)
num2 = num.copy()
num.append(10)
print("The copy list is",num2)

# WAP to remove the duplicates in a list.
numbers = [2,2,3,4,5,5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print("The uniques numbers are:",uniques)