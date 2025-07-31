class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class Queue:
    def __init__(self)-> None:
        self.head: Node | None = None
        self.tail: Node | None = None 
        self._size = 0

    def is_empty(self):
        return (self.head == None) 
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node 
                self.tail = new_node
        self._size += 1

    def dequeue(self):
        # handle empty queue
        if self.is_empty():
            raise IndexError("cannot dequeue from empty queue")
        else:
            if self.head:
                data = self.head.data 
                self.head = self.head.next
                if self.head is None:
                    self.tail = None 
                self._size -= 1
                return data
        
    def front(self):
        """Returns the item at the front of the queue without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.head.data #type:ignore

    def size(self):
        """Returns the number of items in the queue. O(1)"""
        return self.size

    def display(self):
        """Displays the queue from front to rear."""
        if self.is_empty():
            print("Queue: []")
            return
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Queue (Front to Rear): [", ", ".join(map(str, elements)), "]")

