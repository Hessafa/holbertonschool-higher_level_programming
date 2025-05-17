#!/usr/bin/python3
"""
Module for text_indentation function.
"""
def text_indentation(text):
    """Function that prints a text with two new lines after each of these characters: `.`, `?`, and `:`.

    Args:
    text (str): The text to be printed.

    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")  # Print the current character without a newline
        if text[i] in ['.', '?', ':']:  # Check if it's one of the characters that needs to be followed by newlines
            print("\n")  # Print a new line
        i += 1
