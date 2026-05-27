import unittest
from io import StringIO
import sys

# --- Your code ---
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top 
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        return tmp


# --- Unit Tests ---
class TestStack(unittest.TestCase):

    def test_constructor(self):
        """Test that a stack initializes correctly with a starting value."""
        my_stack = Stack(10)
        self.assertIsNotNone(my_stack.top)
        self.assertEqual(my_stack.top.value, 10)
        self.assertIsNone(my_stack.top.next)
        self.assertEqual(my_stack.height, 1)

    def test_push(self):
        """Test pushing multiple elements onto the stack."""
        my_stack = Stack(10)
        my_stack.push(20)
        
        self.assertEqual(my_stack.top.value, 20)
        self.assertEqual(my_stack.top.next.value, 10)
        self.assertEqual(my_stack.height, 2)

    def test_pop_standard(self):
        """Test popping an element from a multi-item stack (LIFO order)."""
        my_stack = Stack(10)
        my_stack.push(20)
        
        # Pop the top node (should be 20)
        popped_node = my_stack.pop()
        
        self.assertIsNotNone(popped_node)
        self.assertEqual(popped_node.value, 20)
        self.assertIsNone(popped_node.next)  # Disconnected properly
        
        # The underlying stack state
        self.assertEqual(my_stack.top.value, 10)
        self.assertEqual(my_stack.height, 1)

    def test_pop_until_empty(self):
        """Test popping until the stack becomes completely empty."""
        my_stack = Stack(10)
        
        popped_node = my_stack.pop()
        
        self.assertEqual(popped_node.value, 10)
        self.assertIsNone(my_stack.top)     # top should update to None (10.next)
        self.assertEqual(my_stack.height, 0)

    def test_pop_empty_stack(self):
        """Test popping from a stack that has a height of 0."""
        my_stack = Stack(10)
        my_stack.pop() # Height becomes 0
        
        # Try to pop again
        failed_pop = my_stack.pop()
        
        self.assertIsNone(failed_pop)
        self.assertEqual(my_stack.height, 0)

    def test_print_stack(self):
        """Test that print_stack correctly prints values from top to bottom."""
        my_stack = Stack(10)
        my_stack.push(20)
        
        captured_output = StringIO()
        sys.stdout = captured_output
        my_stack.print_stack()
        sys.stdout = sys.__stdout__
        
        expected_output = "20\n10\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
