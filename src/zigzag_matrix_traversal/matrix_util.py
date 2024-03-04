class MatrixUtil:
    @staticmethod
    def generate_empty_matrix(n, m):
        return [[0 for _ in range(m)] for _ in range(n)]

    @staticmethod
    def set_matrix_cell_value(matrix, i, j, value):
        matrix[i][j] = value
        value += 1
        return matrix, value

    @staticmethod
    def merge_into_arr(matrix):
        arr = []
        for sub_arr in matrix:
            for i in range(len(sub_arr)):
                arr.append(sub_arr[i])
        return arr