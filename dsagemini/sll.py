class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head   
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.tail = new_node

    def display(self):
        current = self.head 
        while current:
            print(current.data, end="->")
            current = current.next
    
    def search(self, key):
        current = self.head 
        while current:
            if current.data == key:
                return True 
            current = current.next
        return False 
    
    def delete_node(self, key):
        current = self.head

        if current and current.data ==  key:
            self.head = current.next 
            current = None 
            return 
        
        prev = None 
        if current == self.tail:
            self.tail = prev 

        while current and current.data != key:
            prev = current 
            current = current.next 

        if current is None:
            print(f"\n{key} not found in this list")
            return 
        
        if prev and current:
            prev.next = current.next
            current = None

        if self.head is None:
            self.tail = None 


# Create a new Linked List
my_list = LinkedList()

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("After appending 10, 20, 30:")
my_list.display()  # Expected: 10 -> 20 -> 30

# Prepend an element
my_list.prepend(5)
print("\nAfter prepending 5:")
my_list.display()  # Expected: 5 -> 10 -> 20 -> 30

# Search for elements
print("\nSearching:")
print(f"Is 20 in the list? {my_list.search(20)}")  # Expected: True
print(f"Is 25 in the list? {my_list.search(25)}")  # Expected: False

# Delete elements
print("\nDeleting:")
my_list.delete_node(20)  # Delete middle
print("After deleting 20:")
my_list.display()  # Expected: 5 -> 10 -> 30

my_list.delete_node(5)  # Delete head
print("After deleting 5:")
my_list.display()  # Expected: 10 -> 30

my_list.delete_node(40)  # Delete non-existent
print("After trying to delete 40:")
my_list.display()  # Expected: 10 -> 30

my_list.delete_node(30)  # Delete last
print("After deleting 30:")
my_list.display()  # Expected: (empty line, or just print statement if no elements)
