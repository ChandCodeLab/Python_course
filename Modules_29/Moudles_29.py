# import the modules
import converters

print(converters.kg_to_lbs(70))


# import the functions from the moudles
from converters import kg_to_lbs

print(kg_to_lbs(66))


# Exercise
def find_max(numbers):
    max =numbers[0]
    for number in numbers:
        if number> max:
            max=number
    return max

print(max)


