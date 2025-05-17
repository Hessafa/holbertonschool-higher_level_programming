#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.
    Returns the number of integers printed.
    """
    printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed += 1
    except IndexError:
        pass
    print()
    return printed
