#!/usr/bin/python3
"""Defines a name-printing function."""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the square.

    Raises:
        TypeError: If size is not an integer or float.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    Returns:
        None
    """
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
