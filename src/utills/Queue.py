from LinkedList import LinkedList


class Queue:
    def __init__(self):
        self.__data = LinkedList()

    def offer(self, element):
        self.__data.add(element)

    def peek(self):
        return self.__data.get_first().element

    def poll(self):
        return self.__data.remove(0).element

    def size(self):
        return self.__data.size()

    def is_empty(self):
        return self.__data.is_empty()

    def __repr__(self):
        return self.__data.__repr__()

    def __str__(self):
        return self.__data.__repr__()
