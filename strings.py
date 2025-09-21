course ='Learn Python with Manoj chand '
course1 = "LEARN python's course"
course2 = 'Learn Python "COURSE"'
print(course)
print(course1)
print(course2)

# Multiple line string

message='''
Hello,
I'm fine.
What about you?

'''
print(message)

# To know the character index number
name = "manoj c"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# index start form the left side or from the last character
print(name[-1])
print(name[-3])


#print the string in the different of the range 
range_index = 'Hello guys'
print(range_index[1:5]) #return the character form the index 1 to index 5
print(range_index[3:])  #return the character form the index 3 to the end 
print(range_index[:5])  #return the character form the initial index to 5
print(range_index[:])  #return the whole string


name = 'Jennifer'
print(name[1:-1]) # output- ennife ;print character form 1 index to excluding last character
