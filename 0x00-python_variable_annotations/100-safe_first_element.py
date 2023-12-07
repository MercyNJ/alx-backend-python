#!/usr/bin/env python3
"""Augment the given code with the correct duck-typed annotations:

# The types of the elems of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None

{'lst': typing.Sequence[typing.Any], 'return': \
    typing.Union[typing.Any, NoneType]}
"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence or
    None if the sequence is empty.
    """

    if lst:
        return lst[0]
    else:
        return None
