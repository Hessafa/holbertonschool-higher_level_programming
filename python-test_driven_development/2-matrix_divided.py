#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number to divide each element by.

    Returns:
        list: A new matrix with each element divided and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Check for missing arguments
    if matrix is None or div is None:
        raise TypeError("Missing arguments")
    
    # Ensure matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure that each row has integers or floats, and the same size
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Ensure div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Handle division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Handle division by inf or nan
    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]

    # Perform division and return new matrix
    return [[round(num / div, 2) for num in row] for row in matrix]
