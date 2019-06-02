"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def solution(tree):
    count, _ = unival_detector(tree)
    return count


def unival_detector(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = unival_detector(root.left)
    right_count, is_right_unival = unival_detector(root.right)
    total_count = right_count + left_count

    if not is_left_unival or not is_right_unival:
        return total_count, False

    if root.left is not None and root.left.value != root.value:
        return total_count, False
    if root.right is not None and root.right.value != root.value:
        return total_count, False

    return 1 + total_count, True
