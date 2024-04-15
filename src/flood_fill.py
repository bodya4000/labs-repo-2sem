from enum import Enum

from src.utills.Queue import Queue


def read_file_text_and_convert_into_array(input_file_name):
    with open(f'../resources/flood_fill/{input_file_name}', 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.replace('‘', "'").replace('’', "'")
        lst = data.replace('\n', '').split(".")
        data_lists = [item.strip("[]").split(', ') for item in lst[0].split('],[')]
        data_lists = [[char.strip(" '") for char in sublist] for sublist in data_lists]

    return data_lists


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"


class Color(Enum):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
    YELLOW = 'Y'
    BLACK = 'X'
    GREY = 'C'


def flood_fill(matrix: list[list[str]], y_pos: int, x_pos: int, color: Color) -> int | list[list[str]]:
    if len(matrix) == 0:
        return -1
    if y_pos < 0 or x_pos < 0 or x_pos >= len(matrix) or y_pos >= len(matrix):
        return -1
    if color not in Color:
        return -1
    start_color = matrix[y_pos][x_pos]
    new_color = color.value
    if start_color == new_color:
        return -1
    queue = Queue()
    painted = set()
    queue.offer(Node(x_pos, y_pos))
    while not queue.is_empty():
        current = queue.poll()
        if current not in painted:
            matrix[current.y][current.x] = new_color
            painted.add(current)
            add_right_field_to_queue(current, matrix, queue, start_color)
            add_left_field_to_queue(current, matrix, queue, start_color)
            add_bottom_field_to_queue(current, matrix, queue, start_color)
            add_top_field_to_queue(current, matrix, queue, start_color)
    return matrix


def add_top_field_to_queue(current, matrix, queue, start_color):
    if current.y - 1 >= 0 and matrix[current.y - 1][current.x] == start_color:
        queue.offer(Node(current.x, current.y - 1))


def add_bottom_field_to_queue(current, matrix, queue, start_color):
    if current.y + 1 < len(matrix) and matrix[current.y + 1][current.x] == start_color:
        queue.offer(Node(current.x, current.y + 1))


def add_left_field_to_queue(current, matrix, queue, start_color):
    if current.x - 1 >= 0 and matrix[current.y][current.x - 1] == start_color:
        queue.offer(Node(current.x - 1, current.y))


def add_right_field_to_queue(current, matrix, queue, start_color):
    if current.x + 1 < len(matrix[0]) and matrix[current.y][current.x + 1] == start_color:
        queue.offer(Node(current.x + 1, current.y))
