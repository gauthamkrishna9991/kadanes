#!/usr/bin/env python3

"""
kadanes


Kadane's Algorithm Module

Source: https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

This module holds the Python Implementation of Kadane's Algorithm.

"""


from typing import List, Optional


def max_sum_subarray_kadanes(arr: List[int]) -> Optional[int]:
    local_max = 0
    global_max: Optional[int] = None

    for ele in arr:
        local_max = max(ele, ele + local_max)
        if global_max is not None:
            global_max = max(global_max, local_max)
        else:
            global_max = local_max

    return global_max
