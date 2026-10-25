class Node:
    def __init__(self,value):
        self.next=None
        self.value=value
class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,value):
        if self.head is None:
            node=Node(value)
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            node=Node(value)
            current.next=node

    def prepend(self,value):
        current=Node(value)
        current.next=self.head
        self.head=current

    def to_list(self):
        result=[]
        current=self.head
        while current is not None:
            result.append(current.value)
            current=current.next
        return result
    
    def reverse(self):
        previous=None
        current=self.head
        while current is not None:
            next_node=current.next
            current.next=previous
            previous=current
            current=next_node
        self.head=previous