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
    
    def add_before(self, value):
        ref = Node(value)

        if None == self.head:
            self.tail = ref
        else:
            ref.next=self.head
            self.head.previous = ref
        self.head = ref

    def add_after(self, value):
        ref = Node(value)

        if None == self.head:
            self.head = ref
        else:
            self.tail.next = ref
            ref.previous = self.tail
        self.tail = ref

    def print_forward(self):
        print("Forward: ->")
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def print_backward(self):
        print("Backward: ->")
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.previous
        

print("printing the Doubly Linkedlist")
dlist =  DoublyLinkedList()

dlist.add_before("A")   # A
dlist.add_before("B")   # B->A
dlist.add_before("C")   # C->B->A
dlist.add_after("D")    # C->B->A->D
dlist.add_after("E")    # C->B->A->D->E

dlist.print_forward()  # C->B->A->D->E
dlist.print_backward() # E->D->A->B->C

