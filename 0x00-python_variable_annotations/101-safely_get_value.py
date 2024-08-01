#!/usr/bin/env python3
"""safely_get_value."""


from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T],
                     key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """Returns the value of a key in a dictionary safely."""
    if key in dct:
        return dct[key]
    else:
        return default
