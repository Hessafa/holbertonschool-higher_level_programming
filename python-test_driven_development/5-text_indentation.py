#!/usr/bin/python3
"""Module that defines a function to indent text properly."""


def text_indentation(text):
    """Prints text with two newlines after each '.', '?' or ':'.

    Args:
        text (str): The input string to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":  # Add newline after these characters
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():  # Print any remaining text
        print(buffer.strip())
