from typing import List


def wanted_end_field(row_pos: int, column_pos: int, rows: int, cols: int) -> bool:
    """
     Checks if the current position is the desired end field for Indiana Jones.

     Parameters:
         row_pos (int): The current row position.
         column_pos (int): The current column position.
         rows (int): The total number of rows in the matrix.
         cols (int): The total number of columns in the matrix.

     Returns:
         bool: True if the position is the desired end field, False otherwise.
     """
    return (column_pos == cols - 1 and row_pos == 0) or (column_pos == cols - 1 and row_pos == rows - 1)


def not_wanted_end_field(row_pos: int, column_pos: int, rows: int, cols: int) -> bool:
    """
    Checks if the current position is an undesired end field for Indiana Jones.

    Parameters:
        row_pos (int): The current row position.
        column_pos (int): The current column position.
        rows (int): The total number of rows in the matrix.
        cols (int): The total number of columns in the matrix.

    Returns:
        bool: True if the position is an undesired end field, False otherwise.
    """
    return column_pos == cols - 1 and 0 < row_pos < rows - 1


def indiana_jones_traversal_row(sneaky_way: List[List[str]],
                                rows: int, cols: int,
                                row_pos: int = 0,
                                column_pos: int = 0,
                                amount_of_ways: int = 0) -> int:
    """
    Traverses the matrix recursively to count the number of ways Indiana Jones can reach the desired end field.

    Parameters:
        sneaky_way (List[List[str]]): The matrix representing the path.
        rows (int): The total number of rows in the matrix.
        cols (int): The total number of columns in the matrix.
        row_pos (int, optional): The current row position. Defaults to 0.
        column_pos (int, optional): The current column position. Defaults to 0.
        amount_of_ways (int, optional): The number of ways found so far. Defaults to 0.

    Returns:
        int: The total number of ways Indiana Jones can reach the desired end field.
    """
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
    """
     Initiates the traversal of the matrix to count the number of ways Indiana Jones can reach the desired end field.

     Parameters:
         sneaky_way (List[List[str]]): The matrix representing the path.
         rows (int): The total number of rows in the matrix.
         cols (int): The total number of columns in the matrix.

     Returns:
         int: The total number of ways Indiana Jones can reach the desired end field.
     """
    total_ways = 0

    for i in range(len(sneaky_way)):
        total_ways += indiana_jones_traversal_row(sneaky_way, row_pos=i, rows=rows, cols=cols)

    return total_ways


def get_next_ways(row_pos: int, column_pos: int, matrix: List[List[str]], cols: int, rows: int) -> List:
    """
    Retrieves the next available positions for traversal.

    Parameters:
        row_pos (int): The current row position.
        column_pos (int): The current column position.
        matrix (List[List[str]]): The matrix representing the path.
        cols (int): The total number of columns in the matrix.
        rows (int): The total number of rows in the matrix.

    Returns:
        List: A list of tuples containing the next available positions for traversal.
    """
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
    """
    Reads the input matrix from a file.

    Parameters:
        path (str): The path to the input file.

    Returns:
        Tuple[int, int, List[List[str]]]: A tuple containing the number of rows, number of columns, and the matrix.
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.split("\n")

        matrix_length = data[0].split(" ")
        col_size = int(matrix_length[0])
        row_size = int(matrix_length[1])

        sneaky_way = [list(data[i]) for i in range(1, len(data))]
    return row_size, col_size, sneaky_way


def read_output(path):
    """
      Reads the output from a file.

      Parameters:
          path (str): The path to the output file.

      Returns:
          int: The output value.
      """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    return int(data)
