from lab1.src.zigzag_matrix_traversal import ZigzagMatrixTraversal
import unittest


class TestZigzag(unittest.TestCase):
    def test_given_array_5_on_5(self):
        zigzag_traversal = ZigzagMatrixTraversal(row_size=5, column_size=5)
        result = zigzag_traversal.perform_zigzag_traversal()

        self.assertEqual(
            result,
            [
                1,
                2,
                6,
                7,
                15,
                3,
                5,
                8,
                14,
                16,
                4,
                9,
                13,
                17,
                22,
                10,
                12,
                18,
                21,
                23,
                11,
                19,
                20,
                24,
                25,
            ],
        )

    def test_given_array_2_on_4(self):
        zigzag_traversal = ZigzagMatrixTraversal(row_size=2, column_size=4)
        result = zigzag_traversal.perform_zigzag_traversal()

        self.assertEqual(result, [1, 2, 5, 6, 3, 4, 7, 8])

    def test_single_line_array(self):
        zigzag_traversal = ZigzagMatrixTraversal(row_size=1, column_size=6)
        result = zigzag_traversal.perform_zigzag_traversal()

        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_single_element_array(self):
        zigzag_traversal = ZigzagMatrixTraversal(row_size=1, column_size=1)
        result = zigzag_traversal.perform_zigzag_traversal()

        self.assertEqual(result, [1])


if __name__ == "__main__":
    unittest.main()
