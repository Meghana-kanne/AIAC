from typing import Generic, List, TypeVar, Optional

"""
task2.py

A small custom Stack implementation that keeps only the latest N operations (default 10).
Includes docstrings, inline comments, and simple test cases that display output when run.
"""


T = TypeVar("T")


class Stack(Generic[T]):
    """
    Simple stack (LIFO) that retains only the most recent `max_size` items.
    When pushing a new item while the stack is full, the oldest item is discarded.

    Attributes:
        max_size: maximum number of items to retain (default 10).
    """

    def __init__(self, max_size: int = 10) -> None:
        if max_size <= 0:
            raise ValueError("max_size must be a positive integer")
        self.max_size = max_size
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """
        Push an item onto the stack. If this causes the stack to exceed max_size,
        the oldest item (bottom of the stack) is removed.
        """
        self._items.append(item)
        # If we exceed capacity, drop the oldest (index 0)
        if len(self._items) > self.max_size:
            del self._items[0]

    def pop(self) -> T:
        """
        Pop and return the top item. Raises IndexError if the stack is empty.
        """
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Optional[T]:
        """
        Return the top item without removing it, or None if the stack is empty.
        """
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Return True if the stack has no items."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the current number of items in the stack."""
        return len(self._items)

    def as_list(self) -> List[T]:
        """
        Return a shallow copy of the stack as a list from bottom (index 0)
        to top (last element).
        """
        return list(self._items)

    def __repr__(self) -> str:
        # Represent the stack with the top on the right
        return f"Stack(top->right, size={self.size()}): {self._items}"


# -------------------------
# Simple test/demo cases
# -------------------------
if __name__ == "__main__":
    # Create the stack that retains only the latest 10 operations
    s = Stack[str](max_size=10)

    print("Pushing 12 operations: op1 .. op12")
    for i in range(1, 13):
        op = f"op{i}"
        s.push(op)
        # show brief status after each push
        print(f" pushed {op} -> size={s.size()}")

    print("\nAfter pushing 12 operations (max_size=10), stack contents (bottom->top):")
    print(s.as_list())  # Expect op3 .. op12

    # Verify only latest 10 retained
    assert s.size() == 10
    assert s.as_list()[0] == "op3"
    assert s.peek() == "op12"
    print(f"\npeek() -> {s.peek()}")

    # Pop a couple of items
    print("\nPopping two items:")
    print(" pop ->", s.pop())
    print(" pop ->", s.pop())
    print("Current stack (bottom->top):", s.as_list())

    # Empty the stack completely and print each popped item
    print("\nPopping remaining items:")
    while not s.is_empty():
        print(" pop ->", s.pop())

    print("\nFinal stack empty? ->", s.is_empty())