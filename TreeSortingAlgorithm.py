
# https://github.com/Haj4li
# Tree sorting is a sorting algorithm that works by building a binary search tree from the elements to be sorted,
# and then traversing the tree in-order to obtain the sorted sequence.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)

    def in_order_traversal(self):
        if self.root is not None:
            self._in_order_traversal(self.root)

    def _in_order_traversal(self, current_node):
        if current_node is not None:
            self._in_order_traversal(current_node.left)
            print(current_node.value)
            self._in_order_traversal(current_node.right)

def tree_sort(array):
    tree = BinarySearchTree()
    for value in array:
        tree.insert(value)
    tree.in_order_traversal()

array = [5, 3, 7, 1, 9, 4, 6, 2, 8]
tree_sort(array)
