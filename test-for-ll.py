import unittest
# Replace 'linked_list' with your actual filename (without .py)
from linked_list import Node, LinkedListNode 

class TestLinkedList(unittest.TestCase):

    # --- Previous Tests ---
    def test_initialization(self):
        ll = LinkedListNode(10)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.length, 1)

    def test_append(self):
        ll = LinkedListNode(10)
        ll.append(20)
        self.assertEqual(ll.tail.value, 20)
        self.assertEqual(ll.length, 2)

    def test_pop(self):
        ll = LinkedListNode(10)
        ll.append(20)
        popped = ll.pop()
        self.assertEqual(popped.value, 20)
        self.assertEqual(ll.length, 1)
        self.assertEqual(ll.tail.value, 10)

    # --- New Tests for Added Methods ---

    def test_prepend(self):
        ll = LinkedListNode(10)
        ll.prepend(5)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.head.next.value, 10)
        self.assertEqual(ll.length, 2)

    def test_pop_first(self):
        ll = LinkedListNode(10)
        ll.append(20)
        popped = ll.pop_first()
        self.assertEqual(popped.value, 10)
        self.assertEqual(ll.head.value, 20)
        self.assertEqual(ll.length, 1)
        # Ensure the popped node is disconnected
        self.assertIsNone(popped.next)

    def test_get(self):
        ll = LinkedListNode(10)
        ll.append(20)
        ll.append(30)
        # Test valid index
        self.assertEqual(ll.get(1).value, 20)
        # Test out of bounds
        self.assertEqual(ll.get(5), 0)

    def test_set_value(self):
        ll = LinkedListNode(10)
        result = ll.set_value(0, 50)
        self.assertTrue(result)
        self.assertEqual(ll.head.value, 50)
        
        # Test invalid index
        result_invalid = ll.set_value(5, 100)
        self.assertFalse(result_invalid)

    def test_insert_middle(self):
        ll = LinkedListNode(10)
        ll.append(30)
        # Insert 20 at index 1: [10, 20, 30]
        ll.insert(1, 20)
        self.assertEqual(ll.get(1).value, 20)
        self.assertEqual(ll.length, 3)

    def test_insert_boundaries(self):
        ll = LinkedListNode(10)
        # Test insert at head via insert method
        ll.insert(0, 5)
        self.assertEqual(ll.head.value, 5)
        
        # NOTE: This test might fail until you fix index >= self.length to index > self.length
        result = ll.insert(2, 15) 
        self.assertTrue(result, "Insert at index == length should work (Append)")
        self.assertEqual(ll.tail.value, 15)

if __name__ == '__main__':
    unittest.main()
