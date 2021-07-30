class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, value):
        insert_node = Node(value)

        if None == self.head:
            self.tail = insert_node
        else:
            insert_node.next=self.head
            self.head.previous = insert_node
        self.head = insert_node

    def insert_at_end(self, value):
        insert_node = Node(value)

        if None == self.head:
            self.head = insert_node
        else:
            self.tail.next = insert_node
            insert_node.previous = self.tail
        self.tail = insert_node
    
    def search_item(self,value):
        item_to_search = self.head
        while item_to_search is not None:
                if item_to_search.value == value:
                    break
                item_to_search = item_to_search.next
        return item_to_search
    
    def insert_after_item(self, search_value, insert_value):
        insert_node = Node(insert_value)
        
        # if list is empty
        if None ==  self.head: return self.insert_at_start(insert_value) 
        
        current = self.search_item(search_value)
         
        # if not found        
        if current is None: return False
        
        # if found at tail
        if current is self.tail: return self.insert_at_end(insert_value) 
       
        # if found in the middle
        current.next.previous = insert_node
        current.next.previous.previous = current
        current.next.previous.next = current.next
        current.next = current.next.previous
        
    def insert_before_item(self, search_value, insert_value):
        insert_node = Node(insert_value)
        
        # # if list is empty
        # if None ==  self.head: return self.insert_at_start(insert_value) 
        
        current = self.search_item(search_value)
         
        # if not found        
        if current is None: return False
        
        # if found at head/tail
        if current is self.head: return self.insert_at_start(insert_value) 
        
        # if found in the middle
        current.previous.next = insert_node
        current.previous.next.next = current
        current.previous.next.previous = current.previous
        current.previous = current.previous.next

    def remove_item(self,search_value):
        node_to_delete = Node(search_value)
        
        current = self.search_item(search_value)
        
        # if not found        
        if current is None: return False
        
        # if found at head
        if current is self.head: 
            self.head = current.next
        
        # if found at tail
        if current.next is not None:
            current.next.previous = current.previous
        
        if current.previous is not None:
            current.previous.next = current.next
        
    def print_forward(self):
        doubly_list = f"\nForward-> "
        current = self.head
        while current is not None:
            doubly_list =  doubly_list +  current.value + " -> "
            current = current.next
        print(doubly_list)

    # def print_backward(self):
        # doubly_list = f"\nBackward-> "
        # current = self.tail
        # while current is not None:
        #     doubly_list =  doubly_list +  current.value + " -> "
        #     current = current.previous
        # print(doubly_list)


# execute the above programm
print()
print(f"printing the Doubly Linkedlist\n")
dlist =  DoublyLinkedList()

dlist.insert_at_start("1")   # A
dlist.insert_at_start("2")   # B->A
# # dlist.insert_at_start("C")   # C->B->A
# dlist.insert_at_end("4")    # C->B->A->D
# dlist.print_forward() 
# # dlist.insert_after_item("Z","P") # item Not found
# dlist.insert_after_item("4","5") # item  found and P is added after X
# dlist.print_forward() 
# dlist.insert_after_item("5","6") # item  found and P is added before  X\
# dlist.print_forward() 
# dlist.insert_before_item("2", "7")
# dlist.print_forward() 
# dlist.insert_before_item("7", "T")
# dlist.print_forward() 
# dlist.insert_at_end("Z")

# dlist.remove_item("5")
# dlist.print_forward() 
# dlist.remove_item("T")
# dlist.print_forward() 
# dlist.remove_item("Z")

dlist.remove_item("2")



dlist.print_forward()  # C->B->A->D->E
# dlist.print_backward() # E->D->A->B->C
# print(dlist)

