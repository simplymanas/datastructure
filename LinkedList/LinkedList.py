class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        ref = Node(value)

        if None == self.head:
            self.head = ref
        else:
            self.tail.next = ref
        self.tail = ref

    def addToFront(self, value):
        ref = Node(value)

        if None == self.head:
            self.head = ref
            self.tail = None
            ref.next = self.head
        else:
            current = self.head
            ref.next = current
            self.head = ref
           

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        

print("printing the Linkedlist")
llist =  LinkedList()
llist.add("5")
llist.add("6")
llist.add("7")
llist.addToFront("2")

llist.addToFront("4")
llist.print()
