class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedListNode:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return False
        tmp = self.tail 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            tmp.prev = None
        self.length -= 1
        return tmp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

        
    def pop_first(self):
        if self.length == 0:
            return False
        
        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            tmp.next = None
            self.head.prev = None
        self.length -= 1
        return tmp

    def print_dll(self):
        tmp = self.head 
        for _ in range(self.length):
            print(tmp.value)
            tmp = tmp.next 

    def get(self, index):
        if index >= self.length or index < 0:
            return None 

        tmp = self.head
        if index < (self.length / 2):
            for _ in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            for _ in range(self.length - 1, index, -1):
                tmp = tmp.prev
        return tmp 

    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        prev = self.get(index - 1)
        after = prev.next 
        new_node = Node(value)

        new_node.prev = prev
        new_node.next = next 
        prev.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index >= self.length or index < 0:
            return 0
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()

        tmp = self.get(index)

        tmp.next.prev = tmp.prev
        tmp.prev.next = tmp.next
        tmp.next = None
        tmp.prev = None

        self.length -= 1
        return True
