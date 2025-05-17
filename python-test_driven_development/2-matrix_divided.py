#!/usr/bin/python3

"""
This module divides all elements of a matrix by a number.
"""

def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a number.
    
    Args:
        matrix (list of list of integers/floats): matrix to be divided
        div (int/float): the number to divide the matrix elements by

    Returns:
        list: new matrix with divided elements
    
    Raises:
        TypeError: if the matrix is not a matrix (list of lists of integers/floats)
        TypeError: if each row of the matrix is not of the same size
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(elm, (int, float)) for row in matrix for elm in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(elm / div, 2) for elm in row] for row in matrix]
