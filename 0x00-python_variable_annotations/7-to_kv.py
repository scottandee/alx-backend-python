#!/usr/bin/env python3
"""This script contains a type-annotated function
`to_kv` that takes a string `k` and an int OR float
`v` as arguments and returns a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function returns a tuple containing the
    parameters that are passed as parameters to the
    function
    """
    return (k, v * v)
