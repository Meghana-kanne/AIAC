
from task2 import Stack

class TestStack(unittest.TestCase):

    def test_push_retains_latest_items(self):
        s = Stack(max_size=10)
        for i in range(1, 13):   # push 12 items
            s.push(f"op{i}")

        self.assertEqual(s.size(), 10)                     # only 10 kept
        self.assertEqual(s.as_list()[0], "op3")            # op1 and op2 removed
        self.assertEqual(s.peek(), "op12")                 # top is latest item

    def test_pop(self):
        s = Stack(max_size=5)
        s.push("a")
        s.push("b")
        s.push("c")

        self.assertEqual(s.pop(), "c")                     # LIFO
        self.assertEqual(s.peek(), "b")
        self.assertEqual(s.size(), 2)

    def test_pop_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push("x")
        self.assertFalse(s.is_empty())

    def test_as_list_order(self):
        s = Stack()
        s.push("x")
        s.push("y")
        self.assertEqual(s.as_list(), ["x", "y"])          # bottom -> top

if __name__ == "__main__":
    unittest.main()
