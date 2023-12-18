#!/usr/bin/env python3
def square_matrix_simple(matrix=[]):
    rslt = [[0 for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rslt[i][j] = matrix[i][j] ** 2
    return rslt       
