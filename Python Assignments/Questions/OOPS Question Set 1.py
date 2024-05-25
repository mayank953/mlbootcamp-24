# Question 1: Implementing a Stack

class Stack:
    """
    Design a Python class named `Stack` to represent a stack data structure.

    Theory:
    A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
    It has two main operations: push and pop.
    - Push: Adds an element to the top of the stack.
    - Pop: Removes and returns the top element from the stack.

    Operations:
    1. Push: Add an element to the top of the stack.
    2. Pop: Remove and return the top element from the stack.
    3. Peek: Return the top element of the stack without removing it.
    4. Is Empty: Check if the stack is empty.
    5. Size: Return the number of elements in the stack.

    Test Cases:
    Test Case 1:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.size() == 2
    assert stack.is_empty() is False

    Test Case 2:
    stack = Stack()
    assert stack.is_empty() is True
    stack.push("A")
    stack.push("B")
    stack.push("C")
    assert stack.pop() == "C"
    assert stack.peek() == "B"
    assert stack.size() == 2
    assert stack.is_empty() is False
    """

    def __init__(self):
        # Initialize an empty list to store the elements of the stack
        pass

    def push(self, item):
        # Add an element to the top of the stack
        pass

    def pop(self):
        # Remove and return the top element from the stack
        pass

    def peek(self):
        # Return the top element of the stack without removing it
        pass

    def is_empty(self):
        # Check if the stack is empty
        pass

    def size(self):
        # Return the number of elements in the stack
        pass


# Question 2: Implementing a Queue

class Queue:
    """
    Design a Python class named `Queue` to represent a queue data structure.

    Theory:
    A queue is a linear data structure that follows the First In, First Out (FIFO) principle. 
    It has two main operations: enqueue and dequeue.
    - Enqueue: Adds an element to the rear of the queue.
    - Dequeue: Removes and returns the front element from the queue.

    Operations:
    1. Enqueue: Add an element to the rear of the queue.
    2. Dequeue: Remove and return the front element from the queue.
    3. Front: Return the front element of the queue without removing it.
    4. Is Empty: Check if the queue is empty.
    5. Size: Return the number of elements in the queue.

    Test Cases:
    Test Case 1:
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front() == 1
    assert queue.dequeue() == 1
    assert queue.size() == 2
    assert queue.is_empty() is False

    Test Case 2:
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    assert queue.dequeue() == "A"
    assert queue.front() == "B"
    assert queue.size() == 2
    assert queue.is_empty() is False
    """

    def __init__(self):
        # Initialize an empty list to store the elements of the queue
        pass

    def enqueue(self, item):
        # Add an element to the rear of the queue
        pass

    def dequeue(self):
        # Remove and return the front element from the queue
        pass

    def front(self):
        # Return the front element of the queue without removing it
        pass

    def is_empty(self):
        # Check if the queue is empty
        pass

    def size(self):
        # Return the number of elements in the queue
        pass
