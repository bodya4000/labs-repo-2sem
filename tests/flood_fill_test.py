from src.flood_fill import flood_fill, Color
import unittest


class TestZigzag(unittest.TestCase):
    def test_given_array_5_on_5(self):
        input_matrix = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        any_black_x_pos = 9
        any_black_y_pos = 3
        result = flood_fill(input_matrix, any_black_y_pos, any_black_x_pos, Color.GREY)

        self.assertEqual(result, [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'C'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'B', 'B', 'B', 'B', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C']])


if __name__ == "__main__":
    unittest.main()
