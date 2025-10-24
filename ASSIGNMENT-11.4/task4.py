class Node:
    """A node in the Binary Search Tree."""

    def __init__(self, data):
        """
        Initialize node with data and children.
        :param data: Value for this node.
        """
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree (BST) implementation.

    Supports element insertion, searching, and in-order traversal.
    """

    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.
        :param value: Value to insert.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Helper method to insert recursively.
        :param node: Current node in the tree.
        :param value: Value to insert.
        """
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
        # If value == node.data, do not insert again (no duplicates in BST).

    def search(self, value):
        """
        Search for a value in the BST.
        :param value: Value to search for.
        :return: True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Helper method to search recursively.
        :param node: Current node.
        :param value: Value to search for.
        :return: True if found, False otherwise.
        """
        if node is None:
            return False
        if value == node.data:
            return True
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:  # value > node.data
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """
        Perform in-order traversal of BST and collect values.
        :return: List of values in in-order (sorted).
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """
        Helper to recursively traverse in-order.
        :param node: Node to traverse from.
        :param result: List to append values to.
        """
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    # Test with a list of integers
    numbers = [7, 3, 9, 1, 5, 8, 10]
    bst = BST()
    for num in numbers:
        bst.insert(num)

    print("In-order Traversal Output (should be sorted):")
    print(bst.inorder_traversal())

    # Search for present and absent elements
    test_values = [5, 7, 2, 10, 12]
    for val in test_values:
        found = bst.search(val)
        if found:
            print(f"Value {val} FOUND in BST.")
        else:
            print(f"Value {val} NOT FOUND in BST.")
