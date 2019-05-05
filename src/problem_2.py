"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].
"""


def solution(integers):
	"""O(N) with division"""

	total = 1
	for integer in integers:
		total *= integer

	results = []
	for integer in integers:
		results.append(total / integer)

	return results


def solution_without_division(integers):
	"""O(N)"""

	before = []
	after = []

	total = 1
	for integer in integers:
		before.append(total)
		total *= integer

	total = 1
	for integer in integers[::-1]:
		after.append(total)
		total *= integer
	after.reverse()

	results = []
	for total_before, total_after in zip(before, after):
		results.append(total_before * total_after)

	return results
