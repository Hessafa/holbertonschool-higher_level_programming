# 📘 Python - if/else, loops, functions

This project covers Python basics involving conditional statements, loops, and function definitions.

**This projectis part my Full Stack Software Engineering studies at Holberton School through the Tuwaiq Academy program**

---

## Requirements
- Python 3.x (Ubuntu 20.04 LTS, Python 3.8.*)
- Files must be executable
- Files should end with a new line
- The first line in every file should be #!/usr/bin/python3
- Code must adhere to PEP 8 (pycodestyle 2.7.*)

## Tasks Breakdown: 

<details>
<summary><strong>0. Positive anything is better than negative nothing</strong></summary>

This program assigns a random number and prints whether it's positive, negative, or zero.

```python
#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
```

</details>


<details>
<summary><strong>1. The last digit</strong></summary>

Prints the last digit of a random number with a message describing it.

```python
#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10 if number >= 0 else -(abs(number) % 10)

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
```

</details>


<details>
<summary><strong>2. Print alphabet</strong></summary>

Prints all lowercase letters.

```python
#!/usr/bin/python3

for letter in range(97, 123):
    print(chr(letter), end="")
```

</details>


<details>
<summary><strong>3. Print alphabet except 'q' and 'e'</strong></summary>

Skips 'q' and 'e' while printing the alphabet.

```python
#!/usr/bin/python3

for letter in range(97, 123):
    if chr(letter) != 'e' and chr(letter) != 'q':
        print(chr(letter), end="")
```

</details>


<details>
<summary><strong>4. Hexadecimal printing</strong></summary>

Prints numbers 0–98 in decimal and hexadecimal.

```python
#!/usr/bin/python3

for num in range(0, 99):
    print(f"{num} = {hex(num)}")
```

</details>


<details>
<summary><strong>5. 00...99</strong></summary>

Prints all numbers from 00 to 99, comma-separated.

```python
#!/usr/bin/python3

for num in range(0, 100):
    print(f"{num:02d}", end=", " if num < 99 else "\n")
```

</details>


<details>
<summary><strong>6. Print all combinations of two digits</strong></summary>

Prints all unique two-digit combinations in ascending order.

```python
#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")
```

</details>


<details>
<summary><strong>7. islower</strong></summary>

Checks if a character is lowercase.

```python
#!/usr/bin/python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')
```

</details>


<details>
<summary><strong>8. To uppercase</strong></summary>

Prints a string in uppercase.

```python
#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
```

</details>


<details>
<summary><strong>9. Print last digit</strong></summary>

Returns and prints the last digit of a number.

```python
#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
```

</details>


<details>
<summary><strong>10. a + b</strong></summary>

Returns the sum of two integers.

```python
#!/usr/bin/python3

def add(a, b):
    return a + b
```

</details>


<details>
<summary><strong>11. a ^ b</strong></summary>

Computes and returns `a` to the power of `b`.

```python
#!/usr/bin/python3

def pow(a, b):
    return a ** b
```

</details>


<details>
<summary><strong>12. Fizz Buzz</strong></summary>

Prints numbers 1 to 100, replacing multiples of 3 with `Fizz`, 5 with `Buzz`, and both with `FizzBuzz`.

```python
#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
```

</details>

---

## Task Breakdown with Functions and Descriptions

| Task # | File | Function | Purpose | Usage |
| ------ | ---- | -------- | ------- | ----- |
| 0 | `0-positive_or_negative.py` | N/A | Prints if number is positive, negative, or zero | Run directly |
| 1 | `1-last_digit.py` | N/A | Prints the last digit and its category | Run directly |
| 2 | `2-print_alphabet.py` | N/A | Prints all lowercase letters | Run directly |
| 3 | `3-print_alphabt.py` | N/A | Prints lowercase letters excluding 'q' and 'e' | Run directly |
| 4 | `4-print_hexa.py` | N/A | Prints numbers from 0–98 in decimal and hex | Run directly |
| 5 | `5-print_comb2.py` | N/A | Prints numbers 00–99 with formatting | Run directly |
| 6 | `6-print_comb3.py` | N/A | Prints all unique 2-digit combinations | Run directly |
| 7 | `7-islower.py` | `islower(c)` | Checks if a character is lowercase | `islower('a')` |
| 8 | `8-uppercase.py` | `uppercase(str)` | Converts string to uppercase | `uppercase("text")` |
| 9 | `9-print_last_digit.py` | `print_last_digit(n)` | Prints and returns last digit | `print_last_digit(98)` |
| 10 | `10-add.py` | `add(a, b)` | Adds two integers | `add(2, 3)` |
| 11 | `11-pow.py` | `pow(a, b)` | Computes `a^b` | `pow(2, 3)` |
| 12 | `12-fizzbuzz.py` | `fizzbuzz()` | Prints FizzBuzz from 1 to 100 | `fizzbuzz()` |

---

## How to Run
To run each Python script, execute the following:

```
./0-positive_or_negative.py
./1-last_digit.py
./2-print_alphabet.py
```
For tasks where functions are defined (like ``islower``, ``uppercase``, etc.), you may need to create a separate testing script (main.py) or use an interactive Python shell to call these functions.

## Troubleshooting
- Ensure the ```#!/usr/bin/python3``` line is at the start of each Python script.

- Make sure all files are executable: ```chmod +x *.py```

- For debugging, add print statements inside your functions to verify they work as expected.

