#!/usr/bin/env python3
"""This script contains a type-annotated function
`sum_mixed_list` which takes a `list mxd_lst` of
integers and floats and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(list_mxd_list: List[Union[int, float]]) -> float:
    """This function returns the sum of elements
    in the list passed as parameter
    """
    sum: float = 0.00
    for num in list_mxd_list:
        sum += num
    return sum
