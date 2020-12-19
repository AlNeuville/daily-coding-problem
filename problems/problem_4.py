"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers
as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""


def solution(integers):
    """Sorting the sequence in place and search the minimal positive integer required."""
    integers.sort()

    min = integers[0]
    for integer in integers:
        if min > 0 and integer > min + 1:
            return min + 1
        else:
            min = integer

    return min + 1
