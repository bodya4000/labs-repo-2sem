from src.game_server import *
import unittest


class TestGameServer(unittest.TestCase):
    def test_first_case(self):
        clients, nodes_info = get_clients_and_routes_from_input("../resources/game_server/first_case_input.txt")
        output_value = get_output_value("../resources/game_server/first_case_output")
        graph = init_vertexes(clients, nodes_info)
        result = find_max_min_latency(graph)
        self.assertEqual(result, output_value)

    def test_second_case(self):
        clients, nodes_info = get_clients_and_routes_from_input("../resources/game_server/second_case_input.txt")
        output_value = get_output_value("../resources/game_server/second_case_output")
        graph = init_vertexes(clients, nodes_info)
        result = find_max_min_latency(graph)
        self.assertEqual(result, output_value)

    def test_third_case(self):
        clients, nodes_info = get_clients_and_routes_from_input("../resources/game_server/third_case_input.txt")
        output_value = get_output_value("../resources/game_server/third_case_output.txt")
        graph = init_vertexes(clients, nodes_info)
        result = find_max_min_latency(graph)
        self.assertEqual(result, output_value)


if __name__ == "__main__":
    unittest.main()
