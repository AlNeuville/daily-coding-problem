"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import json


class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def serialize(tree):
	tree_str = [tree.val, '(']
	if tree.left is not None:
		tree_str.append(serialize(tree.left))
	if tree.right is not None:
		tree_str.append(',')
		tree_str.append(serialize(tree.right))
	tree_str.append(')')
	return ''.join(tree_str)


def deserialize(tree_str):
	if tree_str is None or tree_str == '':
		return None

	v = tree_str.split('(', 1)
	if len(v) == 1:
		return Node(v[0])

	c = v[1].split(',', 1)
	if len(c) == 2:
		return Node(v[0], deserialize(c[0]), deserialize(c[1]))
	else:
		return Node(v[0], deserialize(c[0]))


class NodeEncoder(json.JSONEncoder):
	def default(self, o):
		return o.__dict__


def json_node_decoder(json_object):
	return Node(**json_object)


def serialize_json(tree):
	return json.dumps(tree, cls=NodeEncoder)


def deserialize_json(tree_string):
	return json.loads(tree_string, object_hook=json_node_decoder)
