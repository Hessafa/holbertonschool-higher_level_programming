#!/usr/bin/python3
"""
This module contains a function to print a square with the `#` character.
"""

def print_square(size):
    """
    Prints a square with the `#` character of a given size.

    Args:
        size (int): The size of the square.

    Raises:
        ValueError: If size is less than 0.
        TypeError: If size is not an integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
