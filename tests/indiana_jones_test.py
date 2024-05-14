from src.indiana_jones import *
import unittest


class TestIndianaJones(unittest.TestCase):
    def test_first_case(self):
        row_size, col_size, sneaky_way = read_input_matrix("../resources/indiana_jones/input_1")
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
        out_put = read_output("../resources/indiana_jones/output_1")
        self.assertEqual(result, out_put)

    def test_second_case(self):
        row_size, col_size, sneaky_way = read_input_matrix("../resources/indiana_jones/input_2")
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
        out_put = read_output("../resources/indiana_jones/output_2")
        self.assertEqual(result, out_put)


    def test_third_case(self):
        row_size, col_size, sneaky_way = read_input_matrix("../resources/indiana_jones/input_3")
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
        out_put = read_output("../resources/indiana_jones/output_3")
        self.assertEqual(result, out_put)

if __name__ == "__main__":
    unittest.main()
