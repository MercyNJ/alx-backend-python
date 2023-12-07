#!/usr/bin/env python3
"""Given the parameters and the return values, add type
annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from typing import TypeVar, Mapping, Any, Union, Optional


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary with
    a specified key and default value.
    """

    if key in dct:
        return dct[key]
    else:
        return default
