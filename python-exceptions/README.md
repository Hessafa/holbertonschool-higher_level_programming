# Python Exceptions

This project aimed at teaching the basics of Python exceptions and how to handle errors. In this project, we write Python functions that handle different types of exceptions and print specific messages based on those exceptions.

## Table of Contents
<details>
<summary>Tasks (0 - 6)</summary>

- [Task 0: Safe list printing](#task-0-safe-list-printing)
- [Task 1: Safe printing of an integer](#task-1-safe-printing-of-an-integer)
- [Task 2: Print and count integers](#task-2-print-and-count-integers)
- [Task 3: Integers division with debug](#task-3-integers-division-with-debug)
- [Task 4: Divide a list](#task-4-divide-a-list)
- [Task 5: Raise exception](#task-5-raise-exception)
- [Task 6: Raise a message](#task-6-raise-a-message)

</details>

## Tasks

### Task 0: Safe list printing
The `safe_print_list` function prints `x` elements from a list, handling situations where `x` may be greater than the list length. The function also uses `try`/`except` blocks to catch any index out-of-range errors.

```python
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
```

### Task 1: Safe printing of an integer
The `safe_print_integer` function prints an integer value using the `"{:d}".format()` method. If the value is not an integer, it catches the exception and returns `False`.

```python
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
```

### Task 2: Print and count integers
The `safe_print_list_integers` function prints only the integers in a list, skipping any non-integer values. The function uses a `try`/`except` block to catch errors when a value is not an integer.

```python
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
```

### Task 3: Integers division with debug
The `safe_print_division` function performs integer division, catching any exceptions (like division by zero) and printing the result inside the `finally` block.

```python
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result:", result)
    return result
```

### Task 4: Divide a list
The `list_division` function divides corresponding elements from two lists. It handles various exceptions, such as division by zero, wrong types, and out-of-range errors.

```python
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
```

### Task 5: Raise exception
The `raise_exception` function raises a `TypeError` exception when called.

```python
def raise_exception():
    raise TypeError
```

### Task 6: Raise a message
The `raise_exception_msg` function raises a `NameError` exception with a custom message.

```python
def raise_exception_msg(message=""):
    raise NameError(message)
```

## Functions Used

| Function                    | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| `print()`                    | Used to print values to the console.                                 |
| `format()`                   | A string method used to format output strings.                       |
| `try/except`                 | Used to handle exceptions that may occur during program execution.   |
| `raise`                      | Used to raise specific exceptions.                                  |

