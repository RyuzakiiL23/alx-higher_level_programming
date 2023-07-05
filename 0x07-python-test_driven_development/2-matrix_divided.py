#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix.

    Args:
        matrix (list of lists): The matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: The new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a valid matrix of integers or floats,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to zero.

    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    row_lengths = set(len(row) for row in matrix)

    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = ([[round(element / div, 2)
                    for element in row] for row in matrix])

    return new_matrix
