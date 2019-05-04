"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def simple_solution(numbers, sum):
	"""Complexity : O(N²)"""

	for first in numbers:
		for second in numbers:
			if sum == first + second:
				return True

	return False


def optimized_solution(numbers, sum):
	"""Complexity : O(N) (because finding something in a set is O(1))"""

	s = set()
	for number in numbers:
		if sum - number in s:
			return True
		s.add(number)

	return False
