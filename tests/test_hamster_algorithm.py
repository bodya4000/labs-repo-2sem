from src.hamsters_algorithm import *
import unittest


class TestFindMaxCountHamstersAvailable(unittest.TestCase):

    def test_find_max_count_hamsters_available_and_expect_2(self):
        s = 7
        hamsters = [[1, 2], [2, 2], [3, 1]]
        result = max_hamsters(s, hamsters)
        self.assertEqual(result, 2)

    def test_find_max_count_hamsters_available_and_expect_3(self):
        s = 19
        c = 4
        hamsters = [[5, 0], [2, 2], [5, 1], [1, 4]]
        result = max_hamsters(s, hamsters)
        self.assertEqual(result, 3)

    def test_find_max_count_hamsters_available_and_expect_1(self):
        s = 2
        hamsters = [[1, 50000000], [1, 6000000]]
        result = max_hamsters(s, hamsters)
        self.assertEqual(result, 1)

    def test_4(self):
        s = 1000
        hamsters = [
            [10_000, 1],
            [1000, 1],
            [500, 1],
            [300, 1],
            [700, 1],
            [600, 1],
            [400, 2],
            [50, 80]
            ]
        result = max_hamsters(s, hamsters)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
