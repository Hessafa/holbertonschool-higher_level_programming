#!/usr/bin/python3
"""
This module contains a function that prints "My name is <name>".

Author: Your Name
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): the first name.
        last_name (str, optional): the last name. Defaults to an empty string.

    Raises:
        TypeError: if first_name or last_name is not a string.

    Example:
        say_my_name("John", "Doe")
        Output: My name is John Doe
    """

    # Check if both names are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the full name
    print(f"My name is {first_name} {last_name}")
