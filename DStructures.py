# This file contains the data structures needed for Breadth First and Depth First Search since both need a Stack and a Queue

# Defines a Node class for a linked list
class Node:
    def __init__(self, value):  
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setNext(self, temp):
        self.next = temp

    def setPrev(self, temp):
        self.prev = temp

# Single-ended, Singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):  # Check if the linked list is empty
        return self.head is None

    def is_full(self):  # Check if the linked list is full (not implemented)
        return self.head is not None

    def insert_first(self, v):  # Insert a node at the beginning of the linked list
        newnode = Node(v)
        if self.is_empty():
            self.head = newnode
        else:
            newnode.setNext(self.head)
            self.head = newnode

    def insert_last(self, v):  # Insert a node at the end of the linked list
        newnode = Node(v)
        if self.is_empty():
            self.head = newnode
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(newnode)

    def peek_first(self):  # Get the value of the first node without removing it
        if self.is_empty():
            raise ValueError("Linked list is empty")
        else:
            return self.head.getValue()

    def peek_last(self):  # Get the value of the last node without removing it
        if self.is_empty():
            raise ValueError("Linked list is empty")
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            return current.getValue()

    def remove_first(self):  # Remove and return the first node from the linked list
        if self.is_empty():
            raise ValueError("Linked list is empty")
        else:
            removed_node = self.head
            self.head = self.head.getNext()
            return removed_node

    def remove_last(self):  # Remove and return the last node from the linked list
        if self.is_empty():
            raise ValueError("Linked list is empty")
        else:
            current = self.head
            temp = None
            while current.getNext() is not None:
                temp = current
                current = current.getNext()
            if temp is not None:
                temp.setNext(None)
            else:
                self.head = None
            return current

    def __iter__(self):  # Iterator for the linked list
        self.current = self.head
        return self

    def __next__(self):  # Get the next element in the iteration
        if self.current is not None:
            value = self.current.getValue()
            self.current = self.current.getNext()
            return value
        else:
            raise StopIteration

    def display(self):  # Display all elements in the linked list
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next

    def size(self):  # Get the number of elements in the linked list
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

# Code for DSAstack
class DSAStack:
    def __init__(self, max_size=None):
        self.linked_list = LinkedList()
        self.max_size = max_size

    def push(self, data):  # Push an element onto the stack
        if self.is_full():
            raise ValueError("Stack is full")
        self.linked_list.insert_first(data)

    def pop(self):  # Pop the top element from the stack
        if not self.is_empty():
            self.linked_list.remove_first()
        else:
            raise ValueError("Stack is empty")

    def display(self):  # Display all elements in the stack
        print("Stack:", end=" ")
        self.linked_list.display()

    def top(self):  # Get the top element of the stack without removing it
        if not self.is_empty():
            return self.linked_list.head.getValue()
        else:
            raise ValueError("Stack is empty")

    def size(self):  # Get the number of elements in the stack
        current = self.linked_list.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def is_empty(self):  # Check if the stack is empty
        return self.linked_list.is_empty()

    def is_full(self):  # Check if the stack is full (based on max size)
        if self.max_size is not None:
            return self.size() == self.max_size
        else:
            return False

# Code for DSAQueue
class DSAQueue:
    def __init__(self, max_size=None):
        self.linked_list = LinkedList()
        self.max_size = max_size

    def enqueue(self, item):  # Enqueue an element into the queue
        if self.is_full():
            raise ValueError("Queue is full")
        self.linked_list.insert_first(item)

    def dequeue(self):  # Dequeue an element from the queue
        if not self.is_empty():
            return self.linked_list.remove_first().getValue()
        else:
            raise ValueError("Queue is empty")

    def display(self):  # Display all elements in the queue
        print("Queue:", end=" ")
        self.linked_list.display()

    def is_empty(self):  # Check if the queue is empty
        return self.linked_list.is_empty()

    def peek(self):  # Get the front element of the queue without removing it
        if self.is_empty():
            raise ValueError("Queue is empty")
        else:
            return self.linked_list.peek_last()

    def size(self):  # Get the number of elements in the queue
        return self.linked_list.size()

    def is_full(self):  # Check if the queue is full (based on max size)
        if self.max_size is not None:
            return self.size() == self.max_size
        else:
            return False
