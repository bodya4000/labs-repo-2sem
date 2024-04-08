from src.flood_fill import *
import unittest


class TestZigzag(unittest.TestCase):
    def test_given_array_5_on_5(self):
        input_value = read_file_text_and_convert_into_array("input.txt")
        output_value = read_file_text_and_convert_into_array("output.txt")
        any_black_x_pos = 9
        any_black_y_pos = 3
        result = flood_fill(input_value, any_black_y_pos, any_black_x_pos, Color.GREY)
        print(output_value)
        self.assertEqual(output_value, result)


if __name__ == "__main__":
    unittest.main()
