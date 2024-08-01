#!/usr/bin/env python3

"""
takes a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v and
should be annotated as a float.

"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int OR float v as arguments and returns a tuple.

    Args:
        k (str): The key of the dictionary.
        v (Union[int, float]): The value of the dictionary.

    Returns:
        Tuple[str, float]: A tuple of the key and the square of the value.
    """
    return (k, float(v) ** 2)
