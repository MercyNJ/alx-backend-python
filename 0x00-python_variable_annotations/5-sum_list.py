#!/usr/bin/env python3
"""A type-annotated function sum_list which takes a list
input_list of floats as arg and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.
    """

    return float(sum(input_list))
