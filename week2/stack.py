class StackEmptyError(Exception):
    pass

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,items):
        """Ab kya lihku bhai"""
        self.items.append(items)

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("The stack is empty to pop")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmptyError("The stack is Empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

s=Stack()

try:
    print(s.peek())
except StackEmptyError as e:
    print(f"Empty stack: {e}")

try:
    print(s.pop())
except StackEmptyError as e:
    print(f"Empty stack: {e}")