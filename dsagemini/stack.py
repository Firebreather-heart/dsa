class Stack:
    def __init__(self) -> None:
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, data):
        self._items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def size(self):
        return len(self._items)

    def display(self):
        """Displays the stack from top to bottom."""
        if self.is_empty():
            print("Stack: []")
            return
        print("Stack (Top to Bottom): [", ", ".join(
            map(str, reversed(self._items))), "]")


def is_balanced(expression):
    stack = Stack()
    mapping = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in mapping.values():  # It's an opening bracket
            stack.push(char)
        elif char in mapping:  # It's a closing bracket
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False  # Mismatched or no opening bracket

    return stack.is_empty()  # True if all brackets have been matched


def is_balanced2(expression):
    stack = Stack()
    mapping = {"(": ")", "[": "]", "{": "}"}

    #look for the first occurence of an item in the mapping
    for char in expression:
        if char in mapping.keys():
            stack.push(char)
            stack.display()
        elif char in mapping.values():
            if stack.is_empty() or char != mapping[stack.pop()]:
                return False
            
    return stack.is_empty()
    

print(f"'((()))' balanced? {is_balanced2('((()))')}")     # True
print(f"'{[()]}' balanced? {is_balanced2('{[()]}')}")     # True
# False (unclosed parenthesis)
print("'{((())' balanced?", f"{is_balanced2('((())')}")
# False (mismatched brackets)
print("'{(()])}' balanced?", f"{is_balanced2('(()])')}")
# False (closing bracket with no opening)
print("'{])}' balanced?", f"{is_balanced2('])')}")
