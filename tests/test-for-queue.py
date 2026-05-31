import sys
from pathlib import Path
import unittest

# 1. Fix the import path so Python can look one directory up
# This finds the 'tests' folder, grabs its parent directory, and adds it to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# 2. Now we can safely import from queue_module
from queue import Queue, Node


class TestQueue(unittest.TestCase):

    def test_constructor(self):
        """Test that a queue initializes correctly with a single value."""
        q = Queue(10)
        self.assertEqual(q.length, 1)
        self.assertIsNotNone(q.first)
        self.assertIsNotNone(q.last)
        self.assertEqual(q.first.value, 10)
        self.assertEqual(q.last.value, 10)
        self.assertIs(q.first, q.last)

    def test_enqueue_to_existing_queue(self):
        """Test enqueuing items into a queue that already has elements."""
        q = Queue(10)
        self.assertTrue(q.enqueue(20))
        self.assertEqual(q.length, 2)
        self.assertEqual(q.first.value, 10)
        self.assertEqual(q.last.value, 20)

        self.assertTrue(q.enqueue(30))
        self.assertEqual(q.length, 3)
        self.assertEqual(q.last.value, 30)

    def test_dequeue_multiple_items(self):
        """Test dequeuing items in a First-In, First-Out (FIFO) manner."""
        q = Queue(10)
        q.enqueue(20)
        q.enqueue(30)

        # First dequeue
        dequeued1 = q.dequeue()
        self.assertIsInstance(dequeued1, Node)
        self.assertEqual(dequeued1.value, 10)
        self.assertNone(dequeued1.next)
        self.assertEqual(q.length, 2)
        self.assertEqual(q.first.value, 20)

        # Second dequeue
        dequeued2 = q.dequeue()
        self.assertEqual(dequeued2.value, 20)
        self.assertEqual(q.length, 1)
        self.assertEqual(q.first.value, 30)
        self.assertIs(q.first, q.last)

    def test_dequeue_to_empty(self):
        """Test dequeuing the last remaining item in the queue."""
        q = Queue(10)
        dequeued = q.dequeue()
        
        self.assertEqual(dequeued.value, 10)
        self.assertEqual(q.length, 0)
        self.assertNone(q.first)
        self.assertNone(q.last)

    def test_dequeue_from_empty_queue(self):
        """Test that dequeuing from an empty queue returns None."""
        q = Queue(10)
        q.dequeue()
        
        dequeued = q.dequeue()
        self.assertNone(dequeued)
        self.assertEqual(q.length, 0)

    def test_enqueue_after_emptied(self):
        """Test that enqueue still works perfectly after a queue has been completely emptied."""
        q = Queue(10)
        q.dequeue()
        
        self.assertTrue(q.enqueue(50))
        self.assertEqual(q.length, 1)
        self.assertEqual(q.first.value, 50)
        self.assertEqual(q.last.value, 50)
        self.assertIs(q.first, q.last)


if __name__ == '__main__':
    unittest.main()
