"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def solution(strings, k):
	window = set()
	begin, end = 0, 0
	longest = 0

	for letter in strings:

		end += 1

		if letter not in window:
			if len(window) > k:
				begin += 1
		else:
			for j in range(begin, end):
				old_letter = strings[j]
				window.remove(old_letter)
				begin += 1
				if old_letter == letter:
					break

		window.add(letter)

		if len(window) > longest:
			longest = len(window)

	return longest
