#!/usr/bin/python3
"""Module that defines text_indentation function."""


def text_indentation(text):
    """Prints text with two newlines after each '.', '?', or ':'.
    
    Args:
        text (str): The text to be printed with indentation.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    temp = ''
    for char in text:
        temp += char
        if char in separators:
            print(temp.strip())
            print()
            temp = ''
    if temp.strip():
        print(temp.strip())
