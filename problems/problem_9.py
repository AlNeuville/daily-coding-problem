"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or
negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5
and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def solution(integers):
	temp0, temp1, result = 0, 0, 0

	for i in range(len(integers)):
		if i == 0:
			result = integers[0]
		elif i == 1:
			result = max(integers[0], integers[1])
		else:
			result = max(temp0, temp1 + integers[i])

		temp1 = temp0
		temp0 = result

	return result
