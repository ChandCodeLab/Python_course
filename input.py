name =input("What is Your name ? ")
print (name)
print("Hi" + name )

# Ask two questions: person's name and favourite color.Then , print a message like "Manoj likes blue"

person_name = input('what is your name? ')
favourite_color = input('what is your favourite color? ')
print(person_name + " likes " +  favourite_color)


# Calculate the age of the person with the help of bith date

birth_year=int(input('Birth year:'))
print(type(birth_year))
age =2025 - birth_year     # or int(birth_year)
print(type(age))
print(age)

# type conversion to diffent data type 
#  int() ,float(),bool()


# Ask a user their weight a(in pounds), convert it to kilograms and print on the terminal

weight_in_pounds = float(input("what is your weight ? "))
cvt_in_Kg = weight_in_pounds*2.20462
print("The weight in Kg is: ",cvt_in_Kg)