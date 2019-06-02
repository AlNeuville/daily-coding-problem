"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

def solution(steps):
	temp0, temp1 = 1, 2
	for _ in range(steps - 1):
		temp0, temp1 = temp1, temp0 + temp1
	return temp0


def generalized_solution(steps, integers):
	temp = [0 for _ in range(steps + 1)]
	temp[0] = 1

	for i in range(steps + 1):
		temp[i] += sum(temp[i - integer] for integer in integers if i - integer > 0)
		temp[i] += 1 if i in integers else 0

	return temp[-1]
