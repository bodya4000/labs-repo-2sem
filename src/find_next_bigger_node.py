# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(root: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.right:
        return find_the_most_left(node.right)
    if node == node.parent.left:
        return node.parent.value
    if node == node.parent.right:
        if node.value > node.parent.value:
            return root
        else:
            return node.value
    return node.value


def find_the_most_left(node):
    if not node.left:
        return node.value
    return find_the_most_left(node.left)


