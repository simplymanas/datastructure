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

    def addToBack(self, value):
        ref = Node(value)

        if None == self.head:
            self.tail = ref
            ref.tail = None
            ref.next = None
        else:
            current = self.tail
            current.next = ref
            self.tail = ref

    def remove_item(self, value):
        #delete_node = Node(value)
        node_to_delete = self.head
        
        # oops here need to compare the value
        while (node_to_delete is not None):
        
            if(value is node_to_delete.value):
               
                # if head to be deleted
                if node_to_delete is self.head:
                    self.head = self.head.next
                    return True
                
                # if tail to be deleted
                if node_to_delete is self.tail:
                    # self.tail =
                    self.tail.next = None
                    return True
            node_to_delete = node_to_delete.next
     
        
    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


print("printing the Linkedlist")
llist = LinkedList()
llist.add("5")
llist.add("6")
llist.add("7")
llist.addToFront("2")
llist.addToFront("4")
llist.addToBack("1")
llist.remove_item("7")

llist.print()
