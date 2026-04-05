class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

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
        removed_item = self._front.val
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError()
        return self._front.val

    def __len__(self):
        return self._size


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.add(x)
        while not self.q1.is_empty():
            self.q2.add(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()
