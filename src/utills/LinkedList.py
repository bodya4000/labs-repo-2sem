from typing import Any

from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def add(self, element: int, index: int = None):
        new_node = Node(element)
        if index is None or index == self.__size:
            index = self.__size
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            if index < 0 or index > self.__size:
                return -1
            current_node = self.get(index)
            new_node.prev = current_node.prev
            new_node.next = current_node
            current_node.prev.next = new_node
            current_node.prev = new_node
        self.__size += 1

    def remove(self, index: int):
        if self.is_empty() or index < 0 or index >= self.__size:
            return None
        being_removed = self.get(index)
        if self.__size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.__size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            being_removed.prev.next = being_removed.next
            being_removed.next.prev = being_removed.prev
        self.__size -= 1
        return being_removed

    def get(self, index: int) -> Any | None:
        if index < 0 or index >= self.__size:
            return None
        if index <= self.__size // 2:
            current_node = self.head
            while index > 0:
                current_node = current_node.next
                index -= 1
        else:
            current_node = self.tail
            index = self.__size - index - 1
            while index > 0:
                current_node = current_node.prev
                index -= 1
        return current_node

    def get_first(self) -> Node:
        return self.head

    def get_last(self) -> Node:
        return self.tail

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.__size == 0

    def __repr__(self) -> str:
        node = self.head
        elements = []
        while node:
            elements.append(str(node.element))
            node = node.next
        return "[" + ", ".join(elements) + "]"
