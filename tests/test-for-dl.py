import unittest
from doubly_linked_list import *

# Assuming your code is in a file named doubly_linked_list.py
# from doubly_linked_list import DoublyLinkedListNode, Node

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        # This runs before every single test to give us a fresh list
        self.dll = DoublyLinkedListNode(10)

    def test_init(self):
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.tail.value, 10)
        self.assertEqual(self.dll.length, 1)

    def test_append(self):
        self.assertTrue(self.dll.append(20))
        self.assertEqual(self.dll.length, 2)
        self.assertEqual(self.dll.tail.value, 20)
        self.assertEqual(self.dll.head.next.value, 20)
        self.assertEqual(self.dll.tail.prev.value, 10)

    def test_pop(self):
        self.dll.append(20)
        
        # Pop from list with >1 items
        popped = self.dll.pop()
        self.assertEqual(popped.value, 20)
        self.assertEqual(self.dll.length, 1)
        self.assertEqual(self.dll.tail.value, 10)
        self.assertIsNone(self.dll.head.next)

        # Pop the last remaining item
        popped = self.dll.pop()
        self.assertEqual(popped.value, 10)
        self.assertEqual(self.dll.length, 0)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

        # Pop from empty list
        self.assertFalse(self.dll.pop())

    def test_prepend(self):
        self.assertTrue(self.dll.prepend(5))
        self.assertEqual(self.dll.length, 2)
        self.assertEqual(self.dll.head.value, 5)
        self.assertEqual(self.dll.head.next.value, 10)
        self.assertEqual(self.dll.tail.prev.value, 5)

    def test_pop_first(self):
        self.dll.append(20)
        
        # Pop first from list with >1 items
        popped = self.dll.pop_first()
        self.assertEqual(popped.value, 10)
        self.assertEqual(self.dll.length, 1)
        self.assertEqual(self.dll.head.value, 20)
        
        # Pop the last remaining item
        self.dll.pop_first()
        self.assertEqual(self.dll.length, 0)
        
        # Pop from empty list
        self.assertFalse(self.dll.pop_first())

    def test_get(self):
        self.dll.append(20)
        self.dll.append(30)
        
        # Valid indices
        self.assertEqual(self.dll.get(0).value, 10)
        self.assertEqual(self.dll.get(1).value, 20)
        self.assertEqual(self.dll.get(2).value, 30)
        
        # Boundary tests (Out of bounds)
        self.assertIsNone(self.dll.get(-1))
        self.assertIsNone(self.dll.get(3))

    def test_set(self):
        self.dll.append(20)
        self.assertTrue(self.dll.set(1, 99))
        self.assertEqual(self.dll.get(1).value, 99)
        self.assertFalse(self.dll.set(5, 100)) # Out of bounds

    def test_insert(self):
        self.dll.append(30)
        
        # Insert at head
        self.assertTrue(self.dll.insert(0, 5))
        self.assertEqual(self.dll.head.value, 5)
        self.assertEqual(self.dll.length, 3)
        
        # Insert at tail
        self.assertTrue(self.dll.insert(3, 40))
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.length, 4)

        # Insert in middle
        self.assertTrue(self.dll.insert(2, 20)) # List is now: 5, 10, 20, 30, 40
        self.assertEqual(self.dll.get(2).value, 20)
        self.assertEqual(self.dll.get(1).next.value, 20)
        self.assertEqual(self.dll.get(3).prev.value, 20)
        self.assertEqual(self.dll.length, 5)
        
        # Out of bounds
        self.assertFalse(self.dll.insert(-1, 0))
        self.assertFalse(self.dll.insert(10, 100))

    def test_remove(self):
        self.dll.append(20)
        self.dll.append(30) # List: 10, 20, 30
        
        # Remove middle
        self.assertTrue(self.dll.remove(1))
        self.assertEqual(self.dll.length, 2)
        self.assertEqual(self.dll.head.next.value, 30)
        self.assertEqual(self.dll.tail.prev.value, 10)
        
        # Remove head
        removed = self.dll.remove(0)
        self.assertEqual(removed.value, 10)
        
        # Out of bounds
        self.assertEqual(self.dll.remove(5), 0)

if __name__ == '__main__':
    unittest.main()
