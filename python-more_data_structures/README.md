# Python - More Data Structures: Set, Dictionary

This project focuses on learning and practicing advanced Python data structures, especially **sets** and **dictionaries**. You will perform operations like adding, updating, searching, and converting values using efficient Pythonic methods without importing any modules.

---

## 📄 Function Summary Table

| Task # | Function Name | Purpose |
|--------|-------------------------------|--------------------------------------------------|
| 0      | `square_matrix_simple(matrix)` | Returns a new matrix with each value squared |
| 1      | `search_replace(my_list, search, replace)` | Replaces all occurrences of an element in a list |
| 2      | `uniq_add(my_list)` | Adds all unique integers in a list |
| 3      | `common_elements(set_1, set_2)` | Returns common elements between two sets |
| 4      | `only_diff_elements(set_1, set_2)` | Returns elements only found in one of the sets |
| 5      | `number_keys(a_dictionary)` | Returns the number of keys in a dictionary |
| 6      | `print_sorted_dictionary(a_dictionary)` | Prints dictionary keys and values in alphabetical order |
| 7      | `update_dictionary(a_dictionary, key, value)` | Updates or adds a key/value pair in a dictionary |
| 8      | `simple_delete(a_dictionary, key)` | Deletes a key from a dictionary if it exists |
| 9      | `multiply_by_2(a_dictionary)` | Returns a new dictionary with values multiplied by 2 |
| 10     | `best_score(a_dictionary)` | Returns the key with the highest integer value |
| 11     | `multiply_list_map(my_list, number)` | Multiplies list items by a number using `map()` |
| 12     | `roman_to_int(roman_string)` | Converts a Roman numeral string to an integer |

---

## ✅ Tasks

<details>
<summary><strong>0. Squared simple</strong></summary>

**Function**: `square_matrix_simple(matrix=[])`

**Explanation**:  
Creates a new matrix with each integer squared.

**Example:**
```python
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```
</details>

<details>
<summary><strong>1. Search and replace</strong></summary>

**Function**: `search_replace(my_list, search, replace)`

**Explanation**:  
Replaces all instances of `search` with `replace` in a new list.

**Example:**
```python
Input: [1, 2, 3, 4, 5, 4, 2, 1], search: 2, replace: 89
Output: [1, 89, 3, 4, 5, 4, 89, 1]
```
</details>

<details>
<summary><strong>2. Unique addition</strong></summary>

**Function**: `uniq_add(my_list=[])`

**Explanation**:  
Sums only unique integers in the list.

**Example:**
```python
Input: [1, 2, 3, 1, 4, 2, 5]
Output: 15
```
</details>

<details>
<summary><strong>3. Present in both</strong></summary>

**Function**: `common_elements(set_1, set_2)`

**Explanation**:  
Returns elements that exist in both sets.

**Example:**
```python
Input: {"Python", "C", "Javascript"}, {"Bash", "C", "Ruby"}
Output: {"C"}
```
</details>

<details>
<summary><strong>4. Only differents</strong></summary>

**Function**: `only_diff_elements(set_1, set_2)`

**Explanation**:  
Returns elements that are unique to either set.

**Example:**
```python
Input: {"Python", "C"}, {"Bash", "C"}
Output: {"Python", "Bash"}
```
</details>

<details>
<summary><strong>5. Number of keys</strong></summary>

**Function**: `number_keys(a_dictionary)`

**Explanation**:  
Returns the number of keys in a dictionary.

**Example:**
```python
Input: {'language': 'C', 'number': 13, 'track': 'Low level'}
Output: 3
```
</details>

<details>
<summary><strong>6. Print sorted dictionary</strong></summary>

**Function**: `print_sorted_dictionary(a_dictionary)`

**Explanation**:  
Prints dictionary keys and values sorted alphabetically by keys.

**Example Output:**
```text
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```
</details>

<details>
<summary><strong>7. Update dictionary</strong></summary>

**Function**: `update_dictionary(a_dictionary, key, value)`

**Explanation**:  
Adds or updates a key in the dictionary.

**Example:**
```python
Input: {'language': 'C'}, update: 'language' → 'Python'
Output: {'language': 'Python'}
```
</details>

<details>
<summary><strong>8. Simple delete by key</strong></summary>

**Function**: `simple_delete(a_dictionary, key="")`

**Explanation**:  
Deletes a key from the dictionary if it exists.

**Example:**
```python
Input: {'language': 'C', 'track': 'Low'}, delete: 'track'
Output: {'language': 'C'}
```
</details>

<details>
<summary><strong>9. Multiply by 2</strong></summary>

**Function**: `multiply_by_2(a_dictionary)`

**Explanation**:  
Returns a new dictionary with values multiplied by 2.

**Example:**
```python
Input: {'John': 12, 'Alex': 8}
Output: {'John': 24, 'Alex': 16}
```
</details>

<details>
<summary><strong>10. Best score</strong></summary>

**Function**: `best_score(a_dictionary)`

**Explanation**:  
Returns the key with the highest integer value.

**Example:**
```python
Input: {'John': 12, 'Molly': 16, 'Adam': 10}
Output: 'Molly'
```
</details>

<details>
<summary><strong>11. Multiply by using map</strong></summary>

**Function**: `multiply_list_map(my_list, number)`

**Explanation**:  
Multiplies all values in a list by `number` using `map()`.

**Example:**
```python
Input: [1, 2, 3], number: 4
Output: [4, 8, 12]
```
</details>

<details>
<summary><strong>12. Roman to Integer</strong></summary>

**Function**: `roman_to_int(roman_string)`

**Explanation**:  
Converts a Roman numeral string to an integer.

**Example:**
```python
Input: 'LXXXVII'
Output: 87
```
</details>
