#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += "{:c}".format(ord(char) - 32)  # Convert to uppercase
        else:
            result += char
    print(result)  # Print the result once
