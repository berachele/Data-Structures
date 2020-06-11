class Queue:
    def __init__(self):
        self.storage = []

    def __len__(self):
        length = len(self.storage)
        return length

    def enqueue(self, value):
        add = self.storage.append(value)
        return add

    def dequeue(self):
        if self.__len__() == 0:
            return None
        else:
            return self.storage.pop(0)
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare the value to the root's value to determine which direction to go
        #if value < root's value, go left
        if value < self.value:
            #does it already have a left child though? We don't want to overwrite a value
            if self.left:
                #self.left is a Node
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        #otherwise value >=  root's value, go right
        else:
            if self.right:
                #self.right is a  Node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        #less than value, check left
        elif target < self.value:
            #if on the left side, return True
            if self.left:
                return self.left.contains(target)
            #otherwise return False
            else:
                return False
        #greater than value, check right
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        #get very right side
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        #recursion get for each for each value
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part / Day 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        #all the way to the left till not None
        #recurse back up
        if self.left:
            self.left.in_order_print(self)    
        #checking if theres a right
        #at top then going right, if left?/lower?
        #print that value
        print(self.value)
        if self.right:
            self.right.in_order_print(self)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create queue
        que = Queue()
        #add root to queue
        que.enqueue(self)
        #while que is not empty:
        while len(que) > 0:
            #node = head of queue
            myNode = que.dequeue()
            #print value
            print(myNode.value)
            #add children of node to queue
            if myNode.left:
                que.enqueue(myNode.left)
            if myNode.right:
                que.enqueue(myNode.right)
            #pop node off the queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #create stack
        stack = []
        #add root to stack
        stack.append(self)
        #while stack is not empty:
        while len(stack) > 0:
            #node = pop top of stack
            myNode = stack.pop()
            #print value
            print(myNode.value)
            #add children of node to stack
            if myNode.right:
                stack.append(myNode.right)
            if myNode.left:
                stack.append(myNode.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
    #checking parent before child
        #print that value
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self)    
        #checking if theres a right
        #at top then going right, if left?/lower?
        if self.right:
            self.right.pre_order_dft(self)
        

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
    #child before parent
        #at top then going right, if left?/lower?
        if self.left:
            self.left.post_order_dft(self)    
        #checking if theres a right
        if self.right:
            self.right.post_order_dft(self)
        #print that value
        print(self.value)


#TESTER
bst = BSTNode(15)
bst.insert(13)
bst.insert(17)
bst.insert(19)
bst.insert(14)
bst.insert(12)
bst.insert(16)
# # bst.for_each(print)
# bst.in_order_print(bst)
# bst.dft_print(bst)
# # bst.bft_print(bst)