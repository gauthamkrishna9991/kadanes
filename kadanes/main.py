#!/usr/bin/env python3

"""
`kadanes`

Kadane's Algorithm

This module holds the main function for running kadane's algorithm.
"""

from typing import List, Optional

from kadanes.kadanes import max_sum_subarray_kadanes


def main():
    arr: List[int] = list(map(int, input().split()))

    max_subarr_sum = max_sum_subarray_kadanes(arr)

    if max_subarr_sum:
        print(f"Maximum subarray sum is {max_subarr_sum}")
    else:
        print(f"Maximum subarray doesn't exist.")
