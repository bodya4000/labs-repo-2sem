from lab1.src.matrix_util import MatrixUtil


class ZigzagMatrixTraversal:
    def __init__(self, row_size, column_size):
        self.__matrix = MatrixUtil.generate_empty_matrix(row_size, column_size)
        self.__matrix_size = row_size * column_size
        self.__last_row = row_size - 1
        self.__last_column = column_size - 1
        self.__row_pos, self.__column_pos = 0, 0
        self.__traversed = False

    def perform_zigzag_traversal(self):
        count = 1
        direction = 'left'
        count = self.add_value_to_empty_cell(count)

        while not self.__traversed:
            if direction == 'left':
                count = self.__first_step_left_down_traversal(count)
                count = self.__traverse_left_down_diagonal(count)
                direction = 'right'
            elif direction == 'right':
                count = self.__first_step_right_up_traversal(count)
                count = self.__traverse_right_up_diagonal(count)
                direction = 'left'
        return MatrixUtil.merge_into_in_arr(self.__matrix)

    def __traverse_left_down_diagonal(self, count):
        while self.__within_bounds_for_left_down_traversal():
            self.__column_pos -= 1
            self.__row_pos += 1
            count = self.add_value_to_empty_cell(count)
        return count

    def __traverse_right_up_diagonal(self, count):
        while self.__within_bounds_for_right_up_traversal():
            self.__column_pos += 1
            self.__row_pos -= 1
            count = self.add_value_to_empty_cell(count)
        return count

    def __first_step_left_down_traversal(self, count):
        if self.__is_column_pos_on_abroad():
            self.__column_pos += 1
            count = self.add_value_to_empty_cell(count)
        else:
            self.__row_pos += 1
            count = self.add_value_to_empty_cell(count)
        return count

    def __first_step_right_up_traversal(self, count):
        if self.__is_row_pos_on_abroad():
            self.__row_pos += 1
            count = self.add_value_to_empty_cell(count)
        else:
            self.__column_pos += 1
            count = self.add_value_to_empty_cell(count)
        return count

    def add_value_to_empty_cell(self, count):
        if self.__is_count_less_than_matrix_size(count):
            self.__matrix, count = MatrixUtil.set_matrix_cell_value(
                self.__matrix, self.__row_pos, self.__column_pos, count)
        else:
            self.__traversed = True
        return count

    def __within_bounds_for_left_down_traversal(self):
        return self.__column_pos > 0 and self.__row_pos < self.__last_row

    def __within_bounds_for_right_up_traversal(self):
        return self.__row_pos > 0 and self.__column_pos < self.__last_column

    def __is_count_less_than_matrix_size(self, count):
        return count <= self.__matrix_size

    def __is_row_pos_on_abroad(self):
        return self.__row_pos < self.__last_row

    def __is_column_pos_on_abroad(self):
        return self.__column_pos < self.__last_column
