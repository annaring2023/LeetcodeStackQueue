from collections import defaultdict
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


class FreqStack:
    def __init__(self):
        self.freq_map = defaultdict(int)
        self.stacks = defaultdict(Stack)
        self.biggest_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq_map[val] + 1
        self.freq_map[val] = freq
        self.biggest_freq = max(self.biggest_freq, freq)
        self.stacks[freq].push(val)

    def pop(self) -> int:
        item = self.stacks[self.biggest_freq].pop()
        self.freq_map[item] -= 1
        if self.stacks[self.biggest_freq].is_empty():
            self.biggest_freq -= 1
        return item

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
