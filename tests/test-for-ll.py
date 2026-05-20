import unittest
from linked_list import *
# Assuming your code is saved in a file or defined above this test class.
# class Node: ...
# class LinkedListNode: ...

class TestLinkedListNode(unittest.TestCase):

    def test_init(self):
        ll = LinkedListNode(4)
        self.assertEqual(ll.head.value, 4)
        self.assertEqual(ll.tail.value, 4)
        self.assertEqual(ll.length, 1)

    def test_append(self):
        ll = LinkedListNode(1)
        self.assertTrue(ll.append(2))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 2)

    def test_pop(self):
        ll = LinkedListNode(1)
        ll.append(2)
        
        # Pop from list with multiple items
        popped_node = ll.pop()
        self.assertEqual(popped_node.value, 2)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.length, 1)
        
        # Pop from list with 1 item
        popped_node = ll.pop()
        self.assertEqual(popped_node.value, 1)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)
        
        # Pop from empty list
        self.assertIsNone(ll.pop())

    def test_prepend(self):
        ll = LinkedListNode(2)
        self.assertTrue(ll.prepend(1))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 2)
        
        # Test prepend on an empty list
        ll.pop()
        ll.pop()
        ll.prepend(3)
        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 1)

    def test_pop_first(self):
        ll = LinkedListNode(1)
        ll.append(2)
        
        # Pop first from list with multiple items
        popped_node = ll.pop_first()
        self.assertEqual(popped_node.value, 1)
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.length, 1)
        
        # Pop first from list with 1 item
        popped_node = ll.pop_first()
        self.assertEqual(popped_node.value, 2)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)
        
        # Pop first from empty list
        self.assertIsNone(ll.pop_first())

    def test_get(self):
        ll = LinkedListNode(0)
        ll.append(1)
        ll.append(2)
        
        # Valid indexes
        self.assertEqual(ll.get(0).value, 0)
        self.assertEqual(ll.get(1).value, 1)
        self.assertEqual(ll.get(2).value, 2)
        
        # Invalid indexes
        self.assertFalse(ll.get(-1))
        self.assertFalse(ll.get(3))

    def test_set_value(self):
        ll = LinkedListNode(0)
        ll.append(1)
        
        # Valid set
        self.assertTrue(ll.set_value(1, 99))
        self.assertEqual(ll.get(1).value, 99)
        
        # Invalid set
        self.assertFalse(ll.set_value(5, 99))

    def test_insert(self):
        ll = LinkedListNode(0)
        ll.append(2)
        
        # Insert in the middle
        self.assertTrue(ll.insert(1, 1))
        self.assertEqual(ll.get(1).value, 1)
        self.assertEqual(ll.length, 3)
        
        # Insert at the beginning
        self.assertTrue(ll.insert(0, -1))
        self.assertEqual(ll.head.value, -1)
        
        # Insert at the end
        self.assertTrue(ll.insert(4, 3))
        self.assertEqual(ll.tail.value, 3)
        
        # Invalid insert
        self.assertFalse(ll.insert(-1, 99))
        self.assertFalse(ll.insert(10, 99))

    def test_remove(self):
        ll = LinkedListNode(0)
        ll.append(1)
        ll.append(2)
        
        # Remove from the middle
        removed_node = ll.remove(1)
        self.assertEqual(removed_node.value, 1)
        self.assertEqual(ll.length, 2)
        self.assertEqual(ll.head.next.value, 2)
        
        # Remove from the beginning
        removed_node = ll.remove(0)
        self.assertEqual(removed_node.value, 0)
        self.assertEqual(ll.head.value, 2)
        
        # Remove from the end
        ll.append(3)
        removed_node = ll.remove(1)
        self.assertEqual(removed_node.value, 3)
        self.assertEqual(ll.tail.value, 2)
        
        # Invalid remove
        self.assertFalse(ll.remove(-1))
        self.assertFalse(ll.remove(5))

    def test_reverse(self):
        ll = LinkedListNode(1)
        ll.append(2)
        ll.append(3)
        
        ll.reverse()
        
        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.head.next.value, 2)
        self.assertEqual(ll.tail.value, 1)
        self.assertIsNone(ll.tail.next)

if __name__ == '__main__':
    unittest.main()
