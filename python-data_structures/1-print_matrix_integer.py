#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
    
    
print(print_matrix_integer(matrix=[
    [1, 5, 7],
    [3, 7, 8],
    [3, 4, 1]
]
))