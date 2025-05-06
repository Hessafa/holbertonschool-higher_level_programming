#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # Check if the character is lowercase
            print("{:c}".format(ord(char) - 32), end="")  # Convert to uppercase
        else:
            print(char, end="")
    print()  # Newline at the end
