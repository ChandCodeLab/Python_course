# Weight conveter form pounds to kilos and vice-versa

weight = int(input("Weight:"))
unit = input("(L)bs or (K)g:")

if unit.upper() == "L":
    conveter = weight * 0.45
    print(f'You are {conveter} kilos')
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
