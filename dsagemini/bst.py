class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: Node, data):
        if node.data > data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)

        elif node.data < data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)
        if node.data == data:
            pass  # No duplicates allowed

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node: Node | None, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node: Node | None, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._find_min_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)
        return node

    def _find_min_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        elements = []
        self._inorder_recursive_collector(self.root, elements)
        print("In-order Traversal (Sorted):", elements)

    def _inorder_recursive_collector(self, node: Node | None, elements: list):
        if node:
            self._inorder_recursive_collector(node.left, elements)
            elements.append(node.data)
            self._inorder_recursive_collector(node.right, elements)
