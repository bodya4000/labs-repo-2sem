import unittest
from src.islands import *


class TestIslandsAlgo(unittest.TestCase):
    def test_normal_case(self):
        input_file = "../resources/islands/islands_input.csv"
        matrix = read_csv_and_return_matrix(input_file)
        result = warshall(matrix)
        self.assertEqual(result, 24)

    def test_unconnected_islands(self):
        input_file = "../resources/islands/islands_unconnected_input.csv"
        matrix = read_csv_and_return_matrix(input_file)
        result = warshall(matrix)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()