#!/usr/bin/python3
"""
This module defines a function to print a person's full name.

The function takes in the first and last names as arguments, and
prints them in the format "My name is <first_name> <last_name>".
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to display.
        last_name (str, optional): The last name to display. Defaults to an empty string.

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Example:
        say_my_name("John", "Doe")
        Output: My name is John Doe

        say_my_name("Jane")
        Output: My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
