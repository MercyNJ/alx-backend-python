#!/usr/bin/env python3
"""A type-annotated function to_kv that takes a string k
and an int/float v as argS & returns a tuple.The 1st
tuple elem is the string k. The 2nd elem is the
square of the int/float v & should be annotated as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with str & square of the int/float.
    """

    return k, float(v ** 2)
