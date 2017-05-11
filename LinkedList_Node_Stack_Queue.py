class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class StackLinkedList:
    """LIFO Stack implementation using a singly linked list for storage."""

    # -------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next): #initialize nodes fields
            self._element = element  # reference to users element
            self._next = next  # reference to next node
    # ------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None # reference to the head node'
        self._size = 0 # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty('Stack is empty')
        return self._head._element # top of stack is at head of list

    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty( 'Stack is empty ')
        answer = self._head._element
        self._head = self._head._next # bypass the former top node
        self._size -= 1
        return answer

class QueueLinkedList:
    """FIFO queue implementation using a singly linked list for storage."""

    # -------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize nodes fields
            self._element = element  # reference to users element
            self._next = next  # reference to next node

    #---------------------------Queue---------------------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0 # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty( ):
            raise Empty( "Queue is empty" )
        return self._head._element # front aligned with head of list

    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty( ):
            raise Empty( 'Queue is empty ')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty( ):  # special case as queue is empty
            self._tail = None # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None) # node will be new tail node
        if self.is_empty( ):
            self._head = newest # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest # update reference to tail node
        self._size += 1




S = StackLinkedList() # contents: [ ]
S.push(5) # contents: [5]
S.push(3) # contents: [5, 3]
print(len(S)) # contents: [5, 3]; outputs 2
print(S.pop( )) # contents: [5]; outputs 3
print(S.is_empty()) # contents: [5]; outputs False
print(S.pop( )) # contents: [ ]; outputs 5
print(S.is_empty()) # contents: [ ]; outputs True
S.push(7) # contents: [7]
S.push(9) # contents: [7, 9]
print(S.top( )) # contents: [7, 9]; outputs 9
S.push(4) # contents: [7, 9, 4]
print(len(S)) # contents: [7, 9, 4]; outputs 3
print(S.pop( )) # contents: [7, 9]; outputs 4
S.push(6) # contents: [7, 9, 6]

print("-------------------")
Q = QueueLinkedList()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
print(Q.first())
print(len(Q))
print(Q.dequeue())
print(Q.is_empty())
print(Q.dequeue())
print(Q.is_empty())
print(Q.dequeue())


