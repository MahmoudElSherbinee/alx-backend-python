#!/usr/bin/env python3

"""
Annotation
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of an element in a list.

    Args:
        lst (list): The list to get the length of.

    Returns:
        list: The length of the element in the list.
    """
    return [(i, len(i)) for i in lst]
