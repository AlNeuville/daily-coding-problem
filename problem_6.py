"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it
holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has
an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference
pointer functions that converts between nodes and memory addresses.
"""


class Element:
	def __init__(self, value, prev, next):
		self.value = value
		self.both = prev ^ next

	def next_element(self, idx):
		return self.both ^ idx

	def prev_element(self, idx):
		return self.both ^ idx


class XORLinkedList:
	def __init__(self):
		self.mem = []
		self.first = -1
		self.last = -1

	def add(self, value):
		if len(self.mem) == 0:
			element = Element(value, -1, 1)
			self.mem.append(element)

			self.first = 0
			self.last = 0
		else:
			last_elem = self.mem[self.last]
			current_index = last_elem.next_element(self.last)

			element = Element(value, current_index - 1, current_index + 1)
			self.mem.append(element)

			self.last = current_index

	def get(self, index):
		if self.first < 0:
			return None

		current_index = self.first
		element = self.mem[self.first]
		prev_index = self.first - 1
		while True:
			if current_index == index:
				return element

			next_index = element.next_element(prev_index)
			element = self.mem[next_index]
			prev_index = current_index
			current_index = next_index
