from LinkedList import LinkedList


class Stack:
    def __init__(self):
        self.__data = LinkedList()

    def push(self, element):
        self.__data.add(element, 0)
        return element

    def peek(self):
        return self.__data.get_first().element

    def pop(self):
        return self.__data.remove(0).element

    def search(self, element):
        current = self.__data.head
        iterator = 0
        while iterator < self.__data.size():
            if current.element == element:
                return current.index
            current = current.next
            iterator += 1
        return -1

    def is_empty(self):
        return self.__data.is_empty()

    def size(self):
        return self.__data.size()

    def __repr__(self):
        return self.__data.__repr__()
