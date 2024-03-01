import unittest


def get_hamster_need(hamster, neighbours_count):
    return hamster[0] + hamster[1] * neighbours_count


def get_neighbours_needs(neighbours):
    if len(neighbours) == 0:
        return 0

    neighbours_need = 0
    neighbours_count = len(neighbours) - 1
    for neighbour in neighbours:
        current_neighbour_need = get_hamster_need(neighbour, neighbours_count)
        neighbours_need += current_neighbour_need
    return neighbours_need


def find_count_for_current_hamster(index, hamsters, supply, neighbours=None, places_for_hamsters=0):
    if index == len(hamsters):
        return places_for_hamsters
    if neighbours is None:
        neighbours = []

    neighbours_need = get_neighbours_needs(neighbours)
    neighbours_count = len(neighbours)

    current_hamster = hamsters[index]
    current_hamster_need = get_hamster_need(current_hamster, neighbours_count)
    need_of_feed = neighbours_need + current_hamster_need
    if need_of_feed < supply:
        places_for_hamsters += 1
        neighbours.append(hamsters[index])
        return find_count_for_current_hamster(index + 1, hamsters, supply, neighbours, places_for_hamsters)
    else:
        return places_for_hamsters


def find_max_count_hamsters_available(supply, hamsters, count_of_hamsters):
    max_places_for_hamsters = 0
    hamster_index = 0

    while hamster_index <= count_of_hamsters - 1:
        result_count = find_count_for_current_hamster(hamster_index, hamsters, supply)
        if result_count > max_places_for_hamsters:
            max_places_for_hamsters = result_count
        if result_count == count_of_hamsters:
            return result_count
        hamster_index += 1

    return max_places_for_hamsters
