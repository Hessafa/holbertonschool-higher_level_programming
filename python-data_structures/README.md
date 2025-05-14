# 📘 Python - Data Structures: Lists, Tuples

Welcome to this Python project focused on basic **data structures** in Python: **lists** and **tuples**. The tasks here are beginner-friendly and designed to teach how to manipulate data using these structures effectively. 
This is 

**This projectis part my Full Stack Software Engineering studies at Holberton School through the Tuwaiq Academy program**

---

## Requirements

- Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

---

##  Tasks Overview

<details>
<summary>✅ 0. Print a list of integers</summary>

- **Function**: `print_list_integer(my_list=[])`
- **What it does**: Prints each integer in the list on a new line using `str.format()`
- **Example**:
```python
my_list = [1, 2, 3]
print_list_integer(my_list)
```
**Output**:
```
1
2
3
```
</details>

<details>
<summary>✅ 1. Secure access to an element in a list</summary>

- **Function**: `element_at(my_list, idx)`
- **What it does**: Safely returns an element at a given index or `None` if the index is invalid.
- **Example**:
```python
element_at([1, 2, 3], 1)  # ➞ 2
```
</details>

<details>
<summary>✅ 2. Replace element in a list</summary>

- **Function**: `replace_in_list(my_list, idx, element)`
- **What it does**: Replaces the element at a given index with a new one, if the index is valid.
</details>

<details>
<summary>✅ 3. Print a list of integers... in reverse!</summary>

- **Function**: `print_reversed_list_integer(my_list=[])`
- **What it does**: Prints each integer in reverse order using `str.format()`.
</details>

<details>
<summary>✅ 4. Replace in a copy</summary>

- **Function**: `new_in_list(my_list, idx, element)`
- **What it does**: Replaces an element at the index **without modifying** the original list.
</details>

<details>
<summary>✅ 5. Can you C me now?</summary>

- **Function**: `no_c(my_string)`
- **What it does**: Removes all `'c'` and `'C'` characters from a string.
</details>

<details>
<summary>✅ 6. Lists of lists = Matrix</summary>

- **Function**: `print_matrix_integer(matrix=[[]])`
- **What it does**: Prints a matrix (list of lists) of integers using `str.format()`.
</details>

<details>
<summary>✅ 7. Tuples addition</summary>

- **Function**: `add_tuple(tuple_a=(), tuple_b=())`
- **What it does**: Adds the first 2 elements of two tuples. Missing elements are treated as 0.
</details>

<details>
<summary>✅ 8. More returns!</summary>

- **Function**: `multiple_returns(sentence)`
- **What it does**: Returns a tuple containing the length of the string and its first character (or `None` if empty).
</details>

<details>
<summary>✅ 9. Find the max</summary>

- **Function**: `max_integer(my_list=[])`
- **What it does**: Returns the largest integer in the list. Returns `None` if the list is empty.
</details>

<details>
<summary>✅ 10. Only by 2</summary>

- **Function**: `divisible_by_2(my_list=[])`
- **What it does**: Returns a list of `True`/`False` values representing if each element is divisible by 2.
</details>

<details>
<summary>✅ 11. Delete at</summary>

- **Function**: `delete_at(my_list=[], idx=0)`
- **What it does**: Deletes an element at a specific index. If invalid, returns list unchanged.
</details>

<details>
<summary>✅ 12. Switch</summary>

- **What it does**: Swaps the values of two variables `a` and `b` using tuple unpacking.
- **Code**:
```python
a, b = b, a
```
- **Example Output**:
```
a=10 - b=89
```
</details>

---

## Concepts Covered

- Lists & Tuples
- Indexing & slicing
- Conditional logic
- Defensive programming (handling invalid inputs)
- Basic Python syntax
- Using `str.format()` for formatted output
- Tuple unpacking

---

## 📂 Project Structure

```
python-data_structures/
├── 0-print_list_integer.py
├── 1-element_at.py
├── 2-replace_in_list.py
├── 3-print_reversed_list_integer.py
├── 4-new_in_list.py
├── 5-no_c.py
├── 6-print_matrix_integer.py
├── 7-add_tuple.py
├── 8-multiple_returns.py
├── 9-max_integer.py
├── 10-divisible_by_2.py
├── 11-delete_at.py
├── 12-switch.py
├── README.md
```

---

## 💡 How to Run

Make sure each file is executable:
```bash
chmod +x *.py
```

Run a test file:
```bash
./0-main.py
```

---

## Summary Table of Functions Used

| Task # | Function Name                     | Description                                                        |
|--------|-----------------------------------|--------------------------------------------------------------------|
| 0      | `print_list_integer(my_list)`     | Prints all integers in a list, one per line using `str.format()`   |
| 1      | `element_at(my_list, idx)`        | Returns element at given index, or `None` if index is invalid     |
| 2      | `replace_in_list(my_list, idx, element)` | Replaces element at index, modifies original list        |
| 3      | `print_reversed_list_integer(my_list)` | Prints list of integers in reverse order using `str.format()` |
| 4      | `new_in_list(my_list, idx, element)` | Replaces element at index, returns a **copy** of the list        |
| 5      | `no_c(my_string)`                 | Returns a string with all 'c' and 'C' characters removed          |
| 6      | `print_matrix_integer(matrix)`    | Prints a matrix (list of lists) of integers using `str.format()` |
| 7      | `add_tuple(tuple_a, tuple_b)`     | Adds the first 2 elements of two tuples, missing values = 0       |
| 8      | `multiple_returns(sentence)`      | Returns a tuple: length of string and its first character         |
| 9      | `max_integer(my_list)`            | Returns the largest integer in the list, or `None` if empty       |
| 10     | `divisible_by_2(my_list)`         | Returns a list of True/False depending on divisibility by 2       |
| 11     | `delete_at(my_list, idx)`         | Deletes item at a given index if valid                            |
| 12     | `a, b = b, a`                     | Swaps the values of `a` and `b` using tuple unpacking             |

