# 📘 Python - Import & Modules

This project covers how to use modules, import functions, and work with dynamic arguments in Python. It emphasizes clean coding practices, avoiding wildcard imports, and understanding execution behavior on import.

**This projectis part my Full Stack Software Engineering studies at Holberton School through the Tuwaiq Academy program**

 ## Requirements
- Python 3.10 on Ubuntu 22.04 LTS
- No wildcard imports or `__import__`
- All files end with a newline and use `#!/usr/bin/python3`
- Must pass `pycodestyle` (v2.7.\*)

## 🔽 Tasks Breakdown

<details>
<summary><strong>📁 0. Import a simple function</strong></summary>

**File:** `0-add.py`  
**Description:** Imports the `add(a, b)` function from `add_0.py` and prints the result of `1 + 2`.

**Output:**
```
1 + 2 = 3
```
</details>

<details>
<summary><strong>📁 1. My first toolbox!</strong></summary>

**File:** `1-calculation.py`  
**Description:** Imports and uses four functions from `calculator_1.py` to perform basic arithmetic on `a = 10` and `b = 5`.

**Output:**
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```
</details>

<details>
<summary><strong>📁 2. How to make a script dynamic</strong></summary>

**File:** `2-args.py`  
**Description:** Prints the number and values of command-line arguments passed to the script.

**Example:**
```
$ ./2-args.py Hello World
2 arguments:
1: Hello
2: World
```
</details>

<details>
<summary><strong>📁 3. Infinite addition</strong></summary>

**File:** `3-infinite_add.py`  
**Description:** Adds all command-line arguments passed to the script.

**Example:**
```
$ ./3-infinite_add.py 79 10 -40
49
```
</details>

<details>
<summary><strong>📁 4. Who are you?</strong></summary>

**File:** `/tmp/4-hidden_discovery.py`  
**Description:** Lists all names in `hidden_4.pyc` that don’t start with `__`, in alphabetical order.

**Example:**
```
my_secret_santa
print_hidden
print_school
```
</details>

<details>
<summary><strong>📁 5. Everything can be imported</strong></summary>

**File:** `5-variable_load.py`  
**Description:** Imports variable `a` from `variable_load_5.py` and prints it.

**Output:**
```
98
```
</details>

---

## Function Summary Table

| Task # | File Name                | Function/Action                                 | Description                                                  |
|--------|--------------------------|--------------------------------------------------|--------------------------------------------------------------|
| 0      | `0-add.py`               | `add(a, b)` (from `add_0.py`)                    | Adds two integers and prints the result                      |
| 1      | `1-calculation.py`       | `add`, `sub`, `mul`, `div` (from `calculator_1.py`) | Performs basic arithmetic operations                       |
| 2      | `2-args.py`              | Uses `sys.argv`                                  | Prints number of arguments and their values                 |
| 3      | `3-infinite_add.py`      | Uses `int(argv[i])`                              | Sums all arguments passed and prints the result             |
| 4      | `4-hidden_discovery.py`  | Uses `dir()` and filtering                       | Prints names in module that don’t start with `__`           |
| 5      | `5-variable_load.py`     | Imports variable `a` from `variable_load_5.py`   | Prints the value of a pre-defined variable                  |

---
