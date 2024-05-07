from typing import List


def find_next_state(pattern: str, state: int, letter: str) -> int:
    if state < len(pattern) and letter == pattern[state]:
        return state + 1

    current_pattern = pattern[:state] + letter
    for comparison_length in range(state, 0, -1):
        prefix = current_pattern[:comparison_length]
        suffix = current_pattern[-comparison_length:]
        if prefix == suffix:
            return comparison_length

    return 0


def build_finite_automata(pattern: str) -> List[List[int]]:
    letters_of_pattern = list(set(pattern))
    finite_automata = [[0 for _ in letters_of_pattern] for __ in range(len(pattern) + 1)]

    for current_state in range(len(pattern) + 1):
        for current_letter in range(len(letters_of_pattern)):
            finite_automata[current_state][current_letter] = find_next_state(pattern, current_state,
                                                                             letters_of_pattern[current_letter])

    return finite_automata


def find_needle(haystack: str, needle: str) -> List[int]:
    finite_automata = build_finite_automata(needle)
    letters_of_pattern = list(set(needle))

    found_occurrences = []
    state = 0
    for i in range(len(haystack)):
        if haystack[i] in needle:
            index = letters_of_pattern.index(haystack[i])
            state = finite_automata[state][index]
            if state == len(needle):
                if len(found_occurrences) == 0 or found_occurrences[-1] + len(needle) <= i - len(needle) + 1:
                    found_occurrences.append(i - len(needle) + 1)
        else:
            state = 0

    return -1 if len(found_occurrences) == 0 else found_occurrences


print(build_finite_automata("co"))
print(find_needle("crocoocokk", "co"))
