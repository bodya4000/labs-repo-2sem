import random
import unittest
from src.red_black_priority_queue import *

def is_red_black_tree_balanced(root):
    def count_black_nodes(node):
        if node is None:
            return 0
        left_black = count_black_nodes(node.left)
        right_black = count_black_nodes(node.right)
        if left_black != right_black:
            return -1
        return left_black + (node.color == Color.BLACK)

    def is_valid_red_black_tree(node):
        if node is None:
            return True

        if node.color == Color.RED:
            if (node.left and node.left.color == Color.RED) or \
                    (node.right and node.right.color == Color.RED):
                return False

        return is_valid_red_black_tree(node.left) and is_valid_red_black_tree(node.right)

    if root is None:
        return True
    if not is_valid_red_black_tree(root):
        return False
    if count_black_nodes(root) == -1:
        return False

    return True

class TestFindLongestPick(unittest.TestCase):
    def test_delete_max_priority_function(self):
        tree = PriorityQueue()
        tree.insert(1.5, 1)
        tree.insert(2, 2)
        tree.insert(3, 2)
        tree.insert(2, 3)
        tree.insert(3, 4)
        tree.insert(4.3, 5)

        deleted = tree.pop()

        self.assertEqual(deleted, 4.3)

    def test_equal_priority_input_data(self):
        tree = PriorityQueue()
        tree.insert(1, 1)
        tree.insert(2, 1)
        tree.insert(3, 1)
        tree.insert(4, 1)
        tree.insert(5, 1)

        self.assertEqual(tree.root.left.element, 4)

    def test_increasing_priority_input_data(self):
        tree = PriorityQueue()
        tree.insert(1, 1)
        tree.insert(11, 2)
        tree.insert(111, 3)
        tree.insert(1111, 4)
        tree.insert(11111, 5)
        self.assertEqual(tree.root.left.element, 1111)

    def test_with_300random_generated_values(self):
        tree = PriorityQueue()
        for i in range(300):
            random_num = random.randint(0, 89)
            random_priority = random.randint(0, 89)
            tree.insert(random_num, random_priority)

        self.assertEqual(is_red_black_tree_balanced(tree.root), True)



if __name__ == "__main__":
    unittest.main()