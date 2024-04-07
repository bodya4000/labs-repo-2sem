import json
import random
from enum import Enum


class Color(Enum):
    RED = "RED"
    BLACK = "BLACK"


class Branch(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Node:
    def __init__(self, element, priority: int):
        self.element = element
        self.priority = priority
        self.parent = None
        self.right = None
        self.left = None
        self.color = Color.RED

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other.color == self.color and other.priority == self.priority and other.element == self.element:
            return True

    def __repr__(self):
        return json.dumps({
            "element": self.element,
            "parent": None if self.parent is None else self.parent.element,
            "left": None if self.left is None else self.left.element,
            "right": None if self.right is None else self.right.element,
            "color": self.color.name,
            "priority": self.priority
        }, indent=2)


def get_uncle(node: Node):
    parent = node.parent
    grandparent = parent.parent
    if parent and grandparent and grandparent.left == parent:
        return grandparent.right
    elif parent and grandparent and grandparent.right == parent:
        return grandparent.left


def switch_color(node: Node):
    if node.color == Color.RED:
        node.color = Color.BLACK
    else:
        node.color = Color.RED


def is_triangle_left_case(node: Node) -> bool:
    parent = node.parent
    grandparent = parent.parent
    if parent and grandparent and grandparent.left == parent and parent.right == node:
        if parent.color == Color.RED:
            return True
    return False


def is_triangle_right_case(node: Node) -> bool:
    parent = node.parent
    grandparent = parent.parent
    if parent and grandparent and grandparent.right == parent and parent.left == node:
        if parent.color == Color.RED:
            return True
    return False


def is_straight_line_left_case(node: Node) -> bool:
    parent = node.parent
    grandparent = parent.parent
    if parent and grandparent and grandparent.left == parent and parent.left == node:
        if parent.color == Color.RED:
            return True
    return False


def is_straight_line_right_case(node: Node) -> bool:
    parent = node.parent
    grandparent = parent.parent
    if parent and grandparent and grandparent.right == parent and parent.right == node:
        if parent.color == Color.RED:
            return True
    return False


def is_red_black_tree_balanced(root):
    def count_black_nodes(node):
        if node is None:
            return 0
        left_black = count_black_nodes(node.left)
        right_black = count_black_nodes(node.right)
        if left_black != right_black:
            return -1
        return left_black + (node.color == Color.BLACK)

    def is_valid_red_black_tree(node):
        if node is None:
            return True

        if node.color == Color.RED:
            if (node.left and node.left.color == Color.RED) or \
                    (node.right and node.right.color == Color.RED):
                return False

        return is_valid_red_black_tree(node.left) and is_valid_red_black_tree(node.right)

    if root is None:
        return True
    if not is_valid_red_black_tree(root):
        return False
    if count_black_nodes(root) == -1:
        return False

    return True


class PriorityQueue:

    def __init__(self):
        self.root = None

    def insert(self, element, priority: int) -> bool:
        new_node = Node(element, priority)
        if not isinstance(priority, int) or priority < 0: return False
        if self.root is None:
            self.root = new_node
        else:
            parent, branch = self.__find_parent(new_node, self.root)
            new_node.parent = parent
            if branch == Branch.LEFT:
                parent.left = new_node
            else:
                parent.right = new_node
        self.__fix_insert(new_node)
        self.root.color = Color.BLACK
        return True

    def __find_parent(self, node: Node, current: Node) -> tuple:
        if node.priority >= current.priority:
            if current.left is None:
                return current, Branch.LEFT
            return self.__find_parent(node, current.left)
        else:
            if current.right is None:
                return current, Branch.RIGHT
        return self.__find_parent(node, current.right)

    def __fix_insert(self, new_node: Node):
        if new_node == self.root:
            self.root.color = Color.BLACK
            return True
        current = new_node
        while current.parent and current.parent.color == Color.RED:
            uncle = get_uncle(current)
            if uncle and uncle.color == Color.RED:
                self.__handle_red_uncle_case(current)
                current = uncle.parent  # here new current is grandparent because I`ve just marked him as red
            elif is_straight_line_left_case(current):
                self.__handle_straight_left_line_case(current)
            elif is_straight_line_right_case(current):
                self.__handle_straight_right_line_case(current)
            elif is_triangle_right_case(current):
                self.__simplify_to_straight_right_line_case(current)
                self.__handle_straight_right_line_case(current.right)
            elif is_triangle_left_case(current):
                self.__simplify_to_straight_left_line_case(current)
                self.__handle_straight_left_line_case(current.left)

    def __handle_red_uncle_case(self, current_node: Node):
        parent = current_node.parent
        uncle = get_uncle(current_node)
        switch_color(parent)
        switch_color(uncle)
        switch_color(parent.parent)

    def __handle_straight_left_line_case(self, current_node: Node):
        parent = current_node.parent
        grandparent = parent.parent
        self.right_rotate(grandparent)
        switch_color(parent)
        switch_color(grandparent)

    def __handle_straight_right_line_case(self, current_node: Node):
        parent = current_node.parent
        grandparent = parent.parent
        self.left_rotate(grandparent)
        switch_color(parent)
        switch_color(grandparent)

    def __simplify_to_straight_right_line_case(self, current_node: Node):
        self.right_rotate(current_node.parent)

    def __simplify_to_straight_left_line_case(self, current_node: Node):
        self.left_rotate(current_node.parent)

    def right_rotate(self, node: Node):
        r"""
            y                  x
           / \                / \
          x   t3    =>       t1  y
        /  \                    / \
       t1   t2                 t2  t3
        """
        if node is None or node.left is None:
            return
        x = node.left
        y = node
        t2 = x.right

        x.right = y
        y.left = t2

        if y.parent:
            if y.parent.left == y:
                y.parent.left = x
            else:
                y.parent.right = x
        else:
            self.root = x
        x.parent = y.parent
        y.parent = x

    def left_rotate(self, node: Node):
        r"""
         x                    y
        / \                  / \
       t1  y       =>       x  t3
          / \              / \
         t2  t3          t1  t2
        """
        if node is None or node.right is None:
            return

        x = node
        y = x.right
        t2 = y.left

        # Perform rotation
        y.left = x
        x.right = t2

        # Update parent pointers
        if t2:
            t2.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        x.parent = y

    def pop(self):
        being_deleted = self.__find_most_left()
        if being_deleted.right:
            being_deleted.parent.left = being_deleted.right
            being_deleted.right.parent = being_deleted.parent
            if being_deleted.color == Color.BLACK:
                self.__fix_delete(being_deleted.right)
        else:
            being_deleted.parent.left = None
            if being_deleted.color == Color.BLACK:
                self.__fix_delete(being_deleted.parent)

        return being_deleted.element

    def __find_most_left(self, current=None):
        if self.root is None: return -1
        if current is None: current = self.root
        if not current.left:
            return current
        return self.__find_most_left(current.left)

    def __fix_delete(self, node):
        while node != self.root and node.color == Color.BLACK:
            parent = node.parent
            sibling = parent.right
            if sibling.color == Color.RED:
                switch_color(sibling)
                switch_color(parent)
                self.left_rotate(parent)
                sibling = parent.right
            if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
                switch_color(sibling)
                node = parent
            else:
                if sibling.color == Color.BLACK:
                    switch_color(sibling.left)
                    switch_color(sibling)
                    self.right_rotate(sibling)
                    sibling = parent.right
                sibling.color = parent.color
                switch_color(parent)
                switch_color(sibling.right)
                self.left_rotate(parent)
                node = self.root

    def in_order_traversal(self, node: Node):
        tasks = []
        if node:
            tasks.extend(self.in_order_traversal(node.left))
            tasks.append(f"task: {node.element}, priority: {node.priority}")
            tasks.extend(self.in_order_traversal(node.right))
        return tasks



if __name__ == '__main__':
    tree = PriorityQueue()
    random_nums = [
        1, 9, 20, 6, 6, 19, 66, 2, 74, 71, 13, 75, 7, 37, 82, 64,
        45, 43, 9, 46, 8, 18, 16, 90, 12, 19, 68, 84, 62, 20, 73,
        63, 41, 96, 12, 42, 82, 40, 7, 73, 87, 0, 34, 89, 69, 85,
        51, 28, 91, 5
    ]

    random_priorities = [
        59, 77, 44, 0, 68, 46, 85, 44, 57, 55, 76, 83, 50, 31, 86,
        14, 9, 9, 51, 76, 99, 45, 73, 38, 45, 13, 68, 33, 85, 36,
        69, 91, 57, 19, 38, 65, 44, 10, 96, 18, 93, 27, 24, 63, 20,
        63, 30, 31, 21, 48
    ]
    for i in range(50):
        if i==12:
            tree.insert(random_nums[i], random_priorities[i])
        else:
            tree.insert(random_nums[i], random_priorities[i])


    print(tree.in_order_traversal(tree.root))
    print(is_red_black_tree_balanced(tree.root))
