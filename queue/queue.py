from collections import deque

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = []
        if self.size is None:
            self.size = 0
        else:
            self.size = self.size

    def __len__(self):
        length = len(self.size)
        return length

    def enqueue(self, value):
        add = self.size.append(value)
        return add

    def dequeue(self):
        drop = deque(self.size)
        remove = drop.popleft()
        if remove is None:
            self.size = 0
        else:
            return self.size
