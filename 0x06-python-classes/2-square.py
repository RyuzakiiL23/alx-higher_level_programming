#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent Square."""

    def __init__(self, size):
        """Initialize The Square."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size