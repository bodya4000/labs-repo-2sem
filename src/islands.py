import heapq


class MinPriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, item))

    def pop(self):
        return heapq.heappop(self._queue)

    def __len__(self):
        return len(self._queue)


def write_output(output_file_path, result):
    file = open(output_file_path, 'w')
    file.write(str(result))
    file.close()


def read_csv_and_return_matrix(input_file):
    matrix = []
    file = open(input_file, 'r')
    try:
        for line in file:
            neighbours = list(map(int, line.split(', ')))
            matrix.append(neighbours)
        file.close()
        return matrix
    except ValueError:
        file.close()
        return


def prims_algorithm(matrix):
    visited = set()
    priority_queue = MinPriorityQueue()
    total_len = 0
    priority_queue.push(0, 0)

    while len(visited) < len(matrix):
        path, current_row = priority_queue.pop()
        if current_row not in visited:
            visited.add(current_row)
            total_len += path
            for i in range(len(matrix)):
                if matrix[current_row][i] != 0 and i not in visited:
                    priority_queue.push(i, matrix[current_row][i])

    return total_len

