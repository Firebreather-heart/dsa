class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Node | None = None
        self.next: Node | None = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None


    def prepend(self, data):
        new_node = Node(data)
        #check empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node 

        else:
            new_node.next = self.head
            self.head.prev = new_node 
            self.head = new_node 

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 

        else:
            new_node.prev = self.tail 
            if self.tail is not None:
                self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, existing_data, new_data):
        pass