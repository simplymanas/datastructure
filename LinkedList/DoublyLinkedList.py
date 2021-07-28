class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None

    def __repr__(self):
        return self.data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addBefore(self, value):
        ref = Node(value)

        if None == self.head:
            self.tail = ref
        else:
            ref.next=self.head
            self.head.previous = ref
        self.head = ref

    def print_forward(self):
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

    def print_backward(self):
            current = self.tail
            while current is not None:
                print(current.value)
                current = current.previous
        

print("printing the Doubly Linkedlist")
dlist =  DoublyLinkedList()
dlist.addBefore("A")
dlist.addBefore("B")
dlist.addBefore("C")
# dlist.print_forward()
dlist.print_backward()

