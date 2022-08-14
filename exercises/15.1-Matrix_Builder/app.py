import random

def matrixBuilder(integer):
    matrix = []

    for i in range(0, integer):
        row = []
        for i in range(0, integer):
            row.append(1)

        matrix.append(row)
    
    return matrix

print(matrixBuilder(3))