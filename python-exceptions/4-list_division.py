#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists index by index.
    Returns a new list with the results of the division.
    If an error occurs, prints an appropriate message and appends 0.
    """
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            continue
    return result
