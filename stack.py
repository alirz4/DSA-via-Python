# Implementing Stack using linked-list

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

my_stack = Stack(1)

my_stack.print_stack()
