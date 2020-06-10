"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        newHead = ListNode(value)

        if not self.head and not self.tail:
            self.head = newHead
            self.tail = newHead
        elif self.head is None:
            self.head = newHead
        else:
            newHead.next = self.head
            self.head.prev = newHead
            self.head = self.head.prev

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value

        if self.head is None and self.tail is None:
            return None
        else:
            self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.✅"""
    def add_to_tail(self, value):
        newTail = ListNode(value)

        if not self.head and not self.tail:
            self.head = newTail
            self.tail = newTail
        elif self.tail is None:
            self.tail = newTail
        else:
            newTail.prev = self.tail
            self.tail.next = newTail
            self.tail = self.tail.next
            
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.✅"""
    def remove_from_tail(self):
        value = self.tail.value

        if self.tail is None and self.head is None:
            return None
        else:
            self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.✅"""
    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail ✅"""
    def delete(self, node):
        #check if node is head or tail (no prev or next)
        if self.head is self.tail:
            self.head = None
            self.tail = None
        #moves pointer pre and next
        elif node is self.head:
            #no prev and a next
            self.head = self.head.next
        elif node is self.tail:
            #has a prev but no next
            self.tail = self.tail.prev
        self.length -= 1
        node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
        
        maxNode = self.head.getValue()

        currentNode = self.head.getNext()

        while currentNode is not None:
            if currentNode.getValue() > maxNode:
                maxNode = currentNode.getValue()
            
            currentNode = currentNode.getNext()

        return maxNode