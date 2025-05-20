# Python - Classes and Objects

This repository contains a series of Python tasks focused on object-oriented programming (OOP), covering topics such as class attributes, instance attributes, methods, and more. These tasks are part of a learning module aimed at understanding basic OOP concepts and applying them in Python.

---

## Tasks Overview

### Task List

<details>
<summary>0. My First Square</summary>

This task introduces creating a simple class for a square.

**Explanation:**
- We created an empty `Square` class.

**Result:**
```python
<class '0-square.Square'>
{}
```

</details>

<details>
<summary>1. Square with Size</summary>

This task focuses on defining a `Square` class with a `size` attribute.

**Explanation:**
- The class is initialized with a `size` attribute.

**Result:**
```python
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
```

</details>

<details>
<summary>2. Size Validation</summary>

In this task, we add size validation to ensure that the `size` attribute is a non-negative integer.

**Explanation:**
- The `size` is validated to ensure it is an integer and greater than or equal to 0.

**Result:**
```python
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
```

</details>

<details>
<summary>3. Area of a Square</summary>

This task introduces a method to calculate the area of the square.

**Explanation:**
- A `area` method is added to calculate the area of the square.

**Result:**
```python
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
```

</details>

<details>
<summary>4. Access and Update Private Attribute</summary>

In this task, we define getters and setters for the `size` attribute and ensure proper validation.

**Explanation:**
- Getters and setters are added to retrieve and set the value of the `size` attribute with validation.

**Result:**
```python
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
```

</details>

<details>
<summary>5. Printing a Square</summary>

This task introduces the `my_print` method to display the square using `#` characters.

**Explanation:**
- A method is added to print the square to the console. If the size is 0, an empty line is printed.

**Result:**
```python
###
###
###
-- 
##########
##########
##########
##########
##########
##########
##########
##########
##########
-- 
-- 
```

</details>

<details>
<summary>6. Coordinates of a Square</summary>

This task adds a `position` attribute to control where the square is printed, supporting both horizontal and vertical offsets.

**Explanation:**
- The `position` is used to control how the square is printed, respecting the tuple of coordinates (x, y).

**Result:**
```python
###
###
###
-- 
_### 
_### 
_### 
-- 
___### 
___### 
___### 
-- 
```

</details>

---

## Functions Used

Here is a table of the functions used in each task:

| Task Number | Function Name | Description |
|-------------|----------------|--------------------------------------------|
| 0           | `__init__`      | Initializes a new `Square` object |
| 1           | `__init__`      | Initializes a new `Square` object with a `size` attribute |
| 2           | `__init__`      | Initializes a new `Square` object with validated `size` |
| 3           | `area`          | Calculates and returns the area of the square |
| 4           | `__init__`      | Initializes a new `Square` object with validated `size` and `position` |
| 4           | `size`          | Getter and setter for the `size` attribute |
| 4           | `position`      | Getter and setter for the `position` attribute |
| 5           | `my_print`      | Prints the square using `#` characters, considering position |
| 6           | `my_print`      | Prints the square using `#` characters, with additional position validation |

---

## How to Run

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/repository-name.git
    ```

2. Navigate into the directory:

    ```bash
    cd repository-name
    ```

3. Run any of the Python scripts directly to test the functionality.

---

## License

This project is part of Holbertonschool and Tuwaiq bootcamp 

