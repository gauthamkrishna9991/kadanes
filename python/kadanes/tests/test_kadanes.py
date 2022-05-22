from kadanes.kadanes import max_sum_subarray_kadanes

# Test Case Elements
test_cases = [
    # Array 1
    ([1, 2, 3, -2, 5], 9),
    # Array 2
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    # Array 3
    ([31, -41, 59, 26, -53, 58, 97, -93, -23, 84], 187),
]


def test_kadanes():
    # For each array and result:
    for arr, result in test_cases:
        # Check the known max-subarray value with kadane's algorithm result.
        assert result == max_sum_subarray_kadanes(arr)
