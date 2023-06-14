#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]

    for x in range(len(new_matrix)):
        for y in range(len(new_matrix[x])):
            new_matrix[x][y] = new_matrix[x][y] * new_matrix[x][y]

    return new_matrix
