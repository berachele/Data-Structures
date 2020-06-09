"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = []
        if self.size is None:
            self.size = 0
        else:
            self.size = self.size

    def __len__(self):
        length = len(self.size)
        return length

    def push(self, value):
        add = self.size.append(value)
        return add

    def pop(self):
        popped = self.size.pop()
        if popped == []:
            return 0
        else:
            return popped
