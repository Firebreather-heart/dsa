class MaxHeap:
    def __init__(self):
        self._heap = []  # Internal list to store heap elements

    def _parent_idx(self, i):
        return (i - 1) // 2

    def _left_child_idx(self, i):
        return 2 * i + 1

    def _right_child_idx(self, i):
        return 2 * i + 2

    def _has_parent(self, i):
        return self._parent_idx(i) >= 0

    def _has_left_child(self, i):
        return self._left_child_idx(i) < len(self._heap)

    def _has_right_child(self, i):
        return self._right_child_idx(i) < len(self._heap)

    def _parent(self, i):
        return self._heap[self._parent_idx(i)] if self._has_parent(i) else None

    def _left_child(self, i):
        return self._heap[self._left_child_idx(i)] if self._has_left_child(i) else None

    def _right_child(self, i):
        return self._heap[self._right_child_idx(i)] if self._has_right_child(i) else None

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _heapify_up(self, index):
        """Restores heap property by bubbling element up."""
        while self._has_parent(index) and self._heap[index] > self._parent(index):
            self._swap(index, self._parent_idx(index))
            index = self._parent_idx(index)  # Move up to the parent's index

    def _heapify_down(self, index):
        """Restores heap property by bubbling element down."""
        larger_child_idx = index
        # Must have at least a left child to go down
        while self._has_left_child(index):
            larger_child_idx = self._left_child_idx(
                index)  # Assume left child is larger

            # Check if right child exists and is larger than left child
            if self._has_right_child(index) and \
               self._right_child(index) > self._left_child(index): # type: ignore
                larger_child_idx = self._right_child_idx(index)

            # If the current node is larger than its largest child, heap property is restored
            if self._heap[index] >= self._heap[larger_child_idx]:
                break
            else:  # Otherwise, swap and continue heapifying down
                self._swap(index, larger_child_idx)
                index = larger_child_idx  # Move down to the larger child's index

    # --- Public API ---

    def is_empty(self):
        return len(self._heap) == 0

    def peek_max(self):
        if self.is_empty():
            raise IndexError("Heap is empty, cannot peek max.")
        return self._heap[0]  # Max element is always at the root (index 0)

    def insert(self, item):
        self._heap.append(item)  # Add to the end
        # Bubble it up from the last index
        self._heapify_up(len(self._heap) - 1)

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Heap is empty, cannot extract max.")

        if len(self._heap) == 1:  # Special case for single element
            return self._heap.pop()

        max_item = self._heap[0]  # Store the root
        self._heap[0] = self._heap.pop()  # Move last element to root
        self._heapify_down(0)  # Bubble new root down
        return max_item

    def size(self):
        return len(self._heap)

    def display(self):
        if self.is_empty():
            print("Heap: []")
            return
        # A simple linear display, not a tree-like visual
        print("Heap (Array Representation):", self._heap)
