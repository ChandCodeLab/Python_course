# (x,y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,2)
# (1,3) ....so on

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")


'''
xxxxx
xx
xxxxx
xx
xx
'''
numbers = [5,2,5,2,2]
for x_count in numbers:
    # print('X' * x_count)
    output=''
    for count in range(x_count):
        output+='x'
    print(output)
    
    
'''
YY
YY
YY
YYYYY
'''
number =[2,2,2,5]
for Y_count in number:
    output =''
    for count in range(Y_count):
        output +='Y'
    print(output)