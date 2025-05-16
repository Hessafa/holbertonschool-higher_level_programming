#!/usr/bin/python3
"""
Module for text_indentation function.
"""

def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', or ':' characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    new_text = ""
    for char in text:
        new_text += char
        if char in chars:
            new_text += "\n\n"

    lines = [line.strip() for line in new_text.split("\n")]
    for line in lines:
        if line:
            print(line)
