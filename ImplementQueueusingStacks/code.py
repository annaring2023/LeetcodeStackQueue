class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class Stack():
    """
    stack
    """
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


class MyQueue:
    def __init__(self):
        self._front = None
        self.s1 = Stack()
        self.s2 = Stack()
    def push(self, x: int) -> None:
        if self.s1.is_empty():
            self._front = x
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

    def pop(self) -> int:
        if self.empty():
            return None
        item = self.s1.pop()
        if not self.s1.is_empty():
            self._front = self.s1.peek()
        else:
            self._front = None
        return item

    def peek(self) -> int:
        return self._front

    def empty(self) -> bool:
        return self.s1.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
