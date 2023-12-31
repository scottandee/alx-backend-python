#!/usr/bin/env python3
"""This script aims at practicing duck typing"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function calculates the length of a list"""
    return [(i, len(i)) for i in lst]
