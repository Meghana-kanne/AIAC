class ListQueue:
    """Queue implementation using Python lists."""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
    
    def is_empty(self):
        return len(self.items) == 0

class DequeQueue:
    """Queue implementation using collections.deque (optimized)."""
    def __init__(self):
        from collections import deque
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("dequeue from empty queue")
    
    def is_empty(self):
        return len(self.items) == 0

def compare_performance():
    import time
    print("Comparing performance of ListQueue vs DequeQueue for 10000 operations...\n")
    num_operations = 10000

    # ListQueue performance
    lq = ListQueue()
    start = time.time()
    for i in range(num_operations):
        lq.enqueue(i)
    for i in range(num_operations):
        lq.dequeue()
    end = time.time()
    listqueue_time = end - start
    print(f"ListQueue total time: {listqueue_time:.6f} seconds")

    # DequeQueue performance
    dq = DequeQueue()
    start = time.time()
    for i in range(num_operations):
        dq.enqueue(i)
    for i in range(num_operations):
        dq.dequeue()
    end = time.time()
    dequequeue_time = end - start
    print(f"DequeQueue total time: {dequequeue_time:.6f} seconds")

    print("\nAI-Generated Performance Comparison:")
    print("-----------------------------------------------------------")
    print("ListQueue uses Python lists, and while appends are fast (O(1)),")
    print("dequeue operations are O(n) because removing from the front")
    print("requires shifting all elements. This becomes inefficient for large queues.")
    print("DequeQueue uses collections.deque, which is optimized for fast appends")
    print("and pops from both ends (O(1) for both enqueue and dequeue).")
    print("As demonstrated above, DequeQueue usually outperforms ListQueue")
    print("on large numbers of enqueue/dequeue operations.")
    print("-----------------------------------------------------------")
    return {"ListQueue_time": listqueue_time, "DequeQueue_time": dequequeue_time}

if __name__ == "__main__":
    compare_performance()
