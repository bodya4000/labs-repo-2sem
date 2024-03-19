import unittest
from src.find_next_bigger_node import *

class TestNextInOrder(unittest.TestCase):
    def test_given_tree(self):
        root = BinaryTree(13)

        root.left = BinaryTree(9)
        root.left.parent = root

        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(11)
        root.left.left.parent = root.left
        root.left.right.parent = root.left

        root.right = BinaryTree(20)
        root.right.parent = root

        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(42)
        root.right.left.parent = root.right
        root.right.right.parent = root.right

        root.right.right.left = BinaryTree(30)
        root.right.right.right = BinaryTree(50)
        root.right.right.left.parent = root.right.right
        root.right.right.right.parent = root.right.right

        root.right.left.left = BinaryTree(14)
        root.right.left.right = BinaryTree(17)
        root.right.left.left.parent = root.right.left
        root.right.left.right.parent = root.right.left

        #         13
        #       /    \
        #      9      20
        #     / \    /   \
        #    3  11  15    42
        #           / \   / \
        #          14 17 30 50
        #
        # In-order traversal: [3, 9, 11, 13, 14, 15, 17, 20, 30, 42, 50]

        result = find_successor(root, root)
        self.assertEqual(result, 14)