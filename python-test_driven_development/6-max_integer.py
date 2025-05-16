#!/usr/bin/python3
"""Module for finding the max integer in a list."""

def max_integer(list=[]):
    """Finds and returns the max integer in a list of integers."""
    if len(list) == 0:
        return None
    result = list[0]
    for i in list:
        if i > result:
            result = i
    return result
