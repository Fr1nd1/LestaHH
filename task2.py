# Первая реализация
class CircularBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

# Вторая реализация
from collections import deque

class CircularBufferDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def is_full(self):
        return len(self.buffer) == self.capacity

    def is_empty(self):
        return len(self.buffer) == 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Buffer is full")
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()
