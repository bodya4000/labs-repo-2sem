class BadParamException(Exception):
    def __init__(self, message="Bad parameter"):
        self.message = message
        super().__init__(self.message)


def find_pattern_index_with_dfa(text: str, pattern: str) -> int:
    state_table = generate_states(pattern)
    current_state = [None, None]
    set_of_pattern_symbol = set(pattern)
    current_index = 0
    found_index = -1
    for index, char in enumerate(text):
        if char not in set_of_pattern_symbol:
            continue
        next_state = get_to_next_state(state_table, current_state)
        if char == next_state[1]:
            if next_state == state_table[-1]:
                found_index = index - len(pattern) + 1
                break
            current_state = next_state
        else:
            if current_state != state_table[0]:
                current_state = [None, None]

    return found_index


def get_to_next_state(state_table: list, current_state):
    if current_state in state_table:
        index_of_current_state = state_table.index(current_state)
        if index_of_current_state + 1 < len(state_table):
            return state_table[index_of_current_state + 1]
        else:
            return BadParamException("Max state")
    else:
        raise BadParamException()


def get_to_prev_state(state_table: list, current_state):
    if current_state in state_table:
        index_of_current_state = state_table.index(current_state)
        if index_of_current_state - 1 >= 0:
            return state_table[index_of_current_state - 1]
        else:
            raise BadParamException("Min state")
    else:
        raise BadParamException("Invalid current state")


def generate_states(pattern: str) -> list:
    patterns = [[None, None]]
    current_symbol = None
    for char in pattern:
        pattern = [current_symbol, char]
        patterns.append(pattern)
        if current_symbol is None:
            current_symbol = char
        else:
            current_symbol += char
    return patterns


states = (generate_states("BLA"))
print(find_pattern_index_with_dfa("hello", "ello"))
