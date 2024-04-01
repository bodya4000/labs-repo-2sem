from enum import Enum
from src.utills.Queue import Queue

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


def flood_fill(matrix: list[list[str]], y_pos: int, x_pos: int, color: Color) -> list[list[str]]:
    new_color = color.value
    queue = Queue()
    painted = set()
    start_color = matrix[y_pos][x_pos]
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