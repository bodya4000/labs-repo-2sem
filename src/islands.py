import heapq
import math

def read_csv_and_return_matrix(input_file: str) -> list[list[int]]:
    """
    reads adj_matrix from file
    """
    adj_matrix = []
    file = open(input_file, 'r')
    try:
        for line in file:
            neighbours = list(map(int, line.split(', ')))
            adj_matrix.append(neighbours)
        file.close()
        return adj_matrix
    except ValueError:
        file.close()
        return [[]]


def warshall(adjacency_matrix: list[list[int]]) -> int:
    num_islands = len(adjacency_matrix)
    total_length = 0
    for k in range(num_islands):
        for i in range(num_islands):
            for j in range(num_islands):
                shortest_path_via_k = adjacency_matrix[i][k] + adjacency_matrix[k][j]
                current_path = adjacency_matrix[i][j]
                if shortest_path_via_k == 0 or current_path == 0:
                    continue
                adjacency_matrix[i][j] = min(current_path, shortest_path_via_k)
                if k == num_islands - 1:
                    total_length += current_path
    return total_length


def iter_current_row(current_row, matrix, priority_queue, visited):
    """
    iterates in row of matrix
    and adds all nodes in it to priority queue
    """
    for i in range(len(matrix)):
        if vertex_has_not_path_or_not_in_visited(current_row, i, matrix, visited):
            priority_queue.push(i, matrix[current_row][i])


def vertex_has_not_path_or_not_in_visited(current_row, i, matrix, visited):
    """
    check if current node is not in visited
    :returns bool
    """
    return matrix[current_row][i] != 0 and i not in visited


if __name__ == '__main__':
    matrix_from_file = read_csv_and_return_matrix("../resources/islands/islands_input.csv")
    matrix = [[0, 3, math.inf, 7], [8, 0, 2, math.inf], [5, math.inf, 0, 1], [2, math.inf, math.inf, 0]]
    print(warshall(matrix_from_file))
    print(matrix_from_file)
