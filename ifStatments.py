is_hot = False
is_cold = False
 
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water ')
elif is_cold:
    print("It's cold day")
    print("Wear warn clothes")
else:    
    print("It's lovey day")
print('Enjoy your day')
    

# Price of a house is $1M
# If buyer has good credit,
#  they need to put down 10%
# otherwise 
    # they need to put down 20%
# print the down payment

price =1000000
has_good_credit =False


if has_good_credit:
   down_payment = 0.1*price
else:
    down_payment = 0.2 *price
print(f'Down payment : ${down_payment}')
   