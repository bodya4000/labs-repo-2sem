import json


class Node:
    def __init__(self, element, index=None):
        self.index = index
        self.element = element
        self.next = None
        self.prev = None
        self.neighbour = set()

    def __eq__(self, other):
        if other.index == self.index:
            return True
        return False

    def __repr__(self):
        return json.dumps({
            "id": self.index,
            "element": self.element,
            "prev": self.prev.element if self.prev else None,
            "next": self.next.element if self.next else None
        })
