import unittest
from src.red_black_priority_queue import *


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


if __name__ == "__main__":
    unittest.main()
