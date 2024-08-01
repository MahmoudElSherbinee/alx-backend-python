#!/usr/bin/env python3

"""
takes a list mxd_lst of integers and floats and returns their sum as a float.

"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of floats.

    Args:
        mxd_lst (list[Union[int, float]]): The list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(mxd_lst)
