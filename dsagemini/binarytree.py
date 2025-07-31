class Node:
    def __init__(self, data):
        self.data = data 
        self.left : Node | None = None 
        self.right : Node | None = None 

    
class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def _in_order_recursive(self, node: Node | None):
        if node:
            self._in_order_recursive(node.left)
            print(node.data, end="")
            self._in_order_recursive(node.right)

    def in_order_traversal(self):
        print("In-order traversal: ", end="")
        self._in_order_recursive(self.root)
        print()

    def _preorder_recursive(self, node: Node | None):
        if node:
            print(node.data, end="")
            self._in_order_recursive(node.left)
            self._in_order_recursive(node.right)

    def preorder_traversal(self):
        print("Pre-order Traversal: ", end="")
        self._preorder_recursive(self.root)
        print()

    def _postorder_recursive(self, node: Node | None):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")

    def postorder_traversal(self):
        print("Post-order Traversal: ", end="")
        self._postorder_recursive(self.root)
        print()
