#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit using modulo
last_digit = number % 10 if number >= 0 else (number % -10) * -1

# Print the required output
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
