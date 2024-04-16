import math
from enum import Enum
from typing import List, Dict, Tuple


class EntityType(Enum):
    CLIENT = "CLIENT"
    ROUTE = "ROUTE"
    SERVER = "SERVER"

    def __repr__(self):
        return self.value


import heapq


class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, priority, task):
        heapq.heappush(self.heap, (priority, task))

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


def get_clients_and_routes_from_input(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.split("\n")
        clients = data[1].split(" ")
        clients = [int(x) for x in clients]
        nodes_info = [list(map(int, string.split())) for string in data[2:]]

    return clients, nodes_info


def get_output_value(path):
    with open(path, 'r') as file:
        value = int(file.read().strip())
    return value


def init_vertexes(clients: List[int], nodes_info: List[List[int]]) -> dict[int, list[tuple[EntityType, int, int]]]:
    graph = {}
    for start_node, end_node, latency in nodes_info:
        if start_node not in graph:
            graph[start_node] = []
        if end_node not in graph:
            graph[end_node] = []

        if start_node in clients:
            graph[start_node].append((EntityType.CLIENT, end_node, latency))
        else:
            graph[start_node].append((EntityType.ROUTE, end_node, latency))

        if end_node in clients:
            graph[end_node].append((EntityType.CLIENT, start_node, latency))
        else:
            graph[end_node].append((EntityType.ROUTE, start_node, latency))

    return graph


def extract_list_of_from_graph_by_entity_type(graph: dict[int, list[tuple[EntityType, int, int]]], type: EntityType):
    lst = []
    for key, value in graph.items():
        entity_type = value[0][0]
        if entity_type == type:
            lst.append(key)
    return lst


def filter_graph_for_clients(graph: dict[int, float], clients: list[int]):
    filtered_graph = {}
    for key, value in graph.items():
        if key in clients:
            filtered_graph[key] = value
    return filtered_graph


def find_max_min_latency(graph: dict[int, list[tuple[EntityType, int, int]]]) -> tuple:
    max_min_path = math.inf
    routes = extract_list_of_from_graph_by_entity_type(graph, EntityType.ROUTE)
    clients = extract_list_of_from_graph_by_entity_type(graph, EntityType.CLIENT)
    server_pos = math.inf
    for route in routes:
        distances = dijkstra(graph, route)
        distances_to_clients = filter_graph_for_clients(distances, clients)
        max_path = max(distances_to_clients.values())
        if max_path < max_min_path:
            max_min_path = max_path
            server_pos = route
    return max_min_path, server_pos


def dijkstra(graph: Dict[int, List[Tuple[EntityType, int, int]]], start_point: int):
    dist_to = {value: math.inf for value in graph.keys()}
    dist_to[start_point] = 0

    queue = MinPriorityQueue()
    visited = set()
    queue.insert(start_point, 0)

    while not queue.is_empty():
        current, current_dist = queue.pop()

        if current in visited:
            continue

        visited.add(current)

        for _, vertex, weight in graph[current]:
            if current_dist + weight < dist_to[vertex]:
                dist_to[vertex] = current_dist + weight
                queue.insert(vertex, dist_to[vertex])

    return dist_to


if __name__ == '__main__':
    clients, nodes_info = get_clients_and_routes_from_input("../resources/game_server/first_case_input.txt")
    output_value = get_output_value("../resources/game_server/first_case_output")
    graph = init_vertexes(clients, nodes_info)
    result = find_max_min_latency(graph)
    self.assertEqual(result, output_value)