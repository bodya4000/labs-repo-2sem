def calculate_max_hamsters_count(first: int, last: int, counted_hamsters: [], supply: int, hamsters: []) -> int:
    mid_index = int((first + last) / 2)
    neighbours_count = mid_index
    hamsters_count = neighbours_count + 1

    tem_arr = sorted([hamster[0] + hamster[1] * neighbours_count for hamster in hamsters])
    need_of_food = sum(tem_arr[:mid_index + 1])
    counted_hamsters[mid_index] = need_of_food
    if need_of_food == supply:
        return hamsters_count
    if need_of_food > supply:
        last = mid_index - 1
        return calculate_max_hamsters_count(first, last, counted_hamsters, supply, hamsters)
    else:
        next_pos = mid_index + 1
        if counted_hamsters[next_pos] > supply:
            return hamsters_count
        first = mid_index + 1
        return calculate_max_hamsters_count(first, last, counted_hamsters, supply, hamsters)


def max_hamsters(supply: int, hamsters: []) -> int:
    first = 0
    last = len(hamsters) - 1
    counted_hamsters = [0] * len(hamsters)

    max_count = calculate_max_hamsters_count(first, last, counted_hamsters, supply, hamsters)

    return max_count


s = 1000
hamsters = [
    [10000, 1],
    [1000, 1],
    [500, 1],
    [300, 1],
    [700, 1],
    [600, 1],
    [400, 2],
    [50, 80]
]
result = max_hamsters(s, hamsters)

print(result)
