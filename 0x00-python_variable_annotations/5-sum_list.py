#!/usr/bin/env python3
"""This script contains a type-annotated function
`sum_list`which takes a list `input_list` of floats
as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function returns the sum of floats in the list
    passed as parameter
    """
    sum: float = 0.00
    for num in input_list:
        sum += num
    return sum
