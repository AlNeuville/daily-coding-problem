"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all
strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def solution(strings, prefix):
	return [string for string in strings if string.startswith(prefix)]


class TrieNode:
	def __init__(self):
		self.children = {}
		self.end = False


class Trie:
	def __init__(self):
		self.root = TrieNode()
		self.word_list = []

	def buildTrie(self, words):
		for word in words:
			self.insert(word)

	def insert(self, word):
		node = self.root

		for letter in list(word):
			if letter not in node.children:
				node.children[letter] = TrieNode()
			node = node.children[letter]

		node.end = True

	def get_words(self, node, word):
		if node.end:
			self.word_list.append(word)

		for letter, child in node.children.items():
			self.get_words(child, word + letter)

	def prefixed_words(self, prefix):
		node = self.root
		not_found = False
		temp_word = ''

		for letter in list(prefix):
			if letter not in node.children:
				not_found = True
				break

			temp_word += letter
			node = node.children[letter]

		if not_found:
			return 0
		elif node.end and not node.children:
			return -1

		self.get_words(node, temp_word)

		return 1


def solution_with_preprocess(strings, prefix):
	trie = Trie()
	trie.buildTrie(strings)

	result = trie.prefixed_words(prefix)
	if result < 0:
		return [prefix]
	elif result == 0:
		return []
	else:
		return trie.word_list
