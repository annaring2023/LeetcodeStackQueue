class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class Stack():
    def __init__(self):
        self.head = None
    def push(self, item):
        self.head = Node(item, next = self.head)
    def pop(self):
        elem = self.head
        self.head = self.head.next
        return elem.val
    def peek(self):
        return self.head.val
    def is_empty(self):
        return self.head is None


class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError()

        removed_item = self._front.item
        self._front = self._front.next

        if self._front is None:
            self._rear = None

        self._size -= 1
        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError()
        return self._front.item

    def __len__(self):
        return self._size

    def __str__(self):
        return f"Queue has {self._size} elements"
