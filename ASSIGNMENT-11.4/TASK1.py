class Stack:
    """A simple Stack implementation using Python list.

    Provides standard stack operations: push, pop, peek, and is_empty.

    Attributes:
        items (list): Internal container for stack elements.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def push(self, item):
        """Push an item onto the stack.

        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.

        Returns:
            The item that was at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item from the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

# Example usage:
if __name__ == "__main__":
    s = Stack()
    print("Is stack empty?", s.is_empty())  # True
    s.push(10)
    s.push(20)
    print("Top item:", s.peek())  # 20
    print("Pop:", s.pop())  # 20
    print("Pop:", s.pop())  # 10
    print("Is stack empty?", s.is_empty())  # True
