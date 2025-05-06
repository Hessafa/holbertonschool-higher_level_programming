#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number (using absolute value for positive numbers)
last_digit = abs(number) % 10

# Check if the number is negative to adjust the last digit correctly
if number < 0:
    last_digit = -last_digit

# Print the result with appropriate condition checks
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last dig of {num} is {last_digit} and is less than 6 and not 0")
