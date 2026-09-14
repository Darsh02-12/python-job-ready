class Stack:
    def __init__(self):
        self.items=[]

    def push(self,items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0