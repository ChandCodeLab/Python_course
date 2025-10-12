

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1]=20  # modify
print(matrix[0][1])
print(matrix[1][1])


# Nested loop

for row in matrix:
    for item in row:
        print(item)