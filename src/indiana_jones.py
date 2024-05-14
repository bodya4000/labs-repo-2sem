from typing import List


def wanted_end_field(row_pos: int, column_pos: int, rows: int, cols: int) -> bool:
    return (column_pos == cols - 1 and row_pos == 0) or (column_pos == cols - 1 and row_pos == rows - 1)


def not_wanted_end_field(row_pos: int, column_pos: int, rows: int, cols: int) -> bool:
    return column_pos == cols - 1 and 0 < row_pos < rows - 1


def indiana_jones_traversal_row(sneaky_way: List[List[str]],
                                rows: int, cols: int,
                                row_pos: int = 0,
                                column_pos: int = 0,
                                amount_of_ways: int = 0) -> int:
    if wanted_end_field(row_pos, column_pos, rows, cols):
        return 1
    if not_wanted_end_field(row_pos, column_pos, rows, cols):
        return 0

    next_available_fields = get_next_ways(row_pos, column_pos, sneaky_way, cols=cols, rows=rows)
    total_ways = 0

    for field in next_available_fields:
        total_ways += indiana_jones_traversal_row(
            sneaky_way,
            row_pos=field[0], column_pos=field[1],
            rows=rows, cols=cols,
            amount_of_ways=amount_of_ways)

    return total_ways


def indiana_jones_traversal(sneaky_way: List[List[str]], rows: int, cols: int) -> int:
    total_ways = 0

    for i in range(len(sneaky_way)):
        total_ways += indiana_jones_traversal_row(sneaky_way, row_pos=i, rows=rows, cols=cols)

    return total_ways


def get_next_ways(row_pos: int, column_pos: int, matrix: List[List[str]], cols: int, rows: int) -> List:
    current_letter = matrix[row_pos][column_pos]
    same_next_letter_positions = []
    for x in range(rows):
        for y in range(column_pos + 1, cols):
            letter = matrix[x][y]
            if letter == current_letter:
                same_next_letter_positions.append((x, y))

    if column_pos + 1 < cols:
        next_pos = (row_pos, column_pos + 1)
        if next_pos not in same_next_letter_positions:
            same_next_letter_positions.append(next_pos)
    return same_next_letter_positions


def read_input_matrix(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.split("\n")

        matrix_length = data[0].split(" ")
        col_size = int(matrix_length[0])
        row_size = int(matrix_length[1])

        sneaky_way = [list(data[i]) for i in range(1, len(data))]
    return row_size, col_size, sneaky_way

def read_output(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    return int(data)

