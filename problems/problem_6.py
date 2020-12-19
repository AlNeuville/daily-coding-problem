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

    def add(self, value):
        if len(self.mem) == 0:
            element = Element(value, -1, 1)
            self.mem.append(element)

            self.first = 0
        else:
            current_index = self.first
            prev_index = self.first - 1
            while True:
                if len(self.mem) <= current_index:
                    element = Element(value, prev_index, current_index + 1)
                    self.mem.insert(current_index + 1, element)
                    return

                element = self.mem[current_index]
                next_index = element.next_element(prev_index)
                prev_index = current_index
                current_index = next_index

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
