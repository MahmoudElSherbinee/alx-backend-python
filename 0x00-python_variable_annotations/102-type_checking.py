#!/usr/bin/env python3
""" Type Annotation Function safely_get_value from a dict """


from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Iterate and zoom in through a list 2x """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
