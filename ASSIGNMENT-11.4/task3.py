class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Implementation of singly linked list with fundamental operations."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        """Insert a new node with 'value' at the end of the list."""
        new_node = Node(value)
        if not self.head:
            # If the list is empty, new node becomes the head.
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            # At the end, set the last node's next to new_node.
            current.next = new_node

    def delete_value(self, value):
        """Delete the first node in the list containing the specified value."""
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    # Bypass current node by pointing previous node's next to current's next.
                    prev.next = current.next
                else:
                    # Node to delete is the head: move head to next node.
                    self.head = current.next
                return True  # Value found and deleted.
            prev = current
            current = current.next
        return False  # Value not found.

    def traverse(self):
        """Return a list of all node values from head to end."""
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

# --------------------- Test Cases ---------------------
# 1. Insert at end in empty and non-empty lists
# 2. Delete head, middle, tail, and non-existent values
# 3. Traverse after each modification

if __name__ == "__main__":
    ll = SinglyLinkedList()
    print("Initial traverse (should be []):", ll.traverse())
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("After inserts (should be [10, 20, 30]):", ll.traverse())

    print("Delete 10 (head) (should be True):", ll.delete_value(10))
    print("Traverse after delete head (should be [20, 30]):", ll.traverse())

    print("Delete 30 (tail) (should be True):", ll.delete_value(30))
    print("Traverse after delete tail (should be [20]):", ll.traverse())

    print("Delete 20 (only node / middle) (should be True):", ll.delete_value(20))
    print("Traverse after delete last (should be []):", ll.traverse())

    print("Delete 42 (non-existent) (should be False):", ll.delete_value(42))
    print("Traverse after trying to delete non-existent:", ll.traverse())

    # Re-insert and traverse
    ll.insert_at_end(100)
    ll.insert_at_end(200)
    print("After more inserts (should be [100, 200]):", ll.traverse())
