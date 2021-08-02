class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None

class Sentinal:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def add_to_back(self, value):
        new_node = Node(value)
        
        #right side
        new_node.next = self.tail
        
        #left side
        new_node.previous = self.tail.previous
        
        new_node.next.previous = new_node.previous.next = new_node
    
    def add_to_front(self,value):
        new_node = Node(value)
        
        #right side
        new_node.next = self.head
        
        #left side
        new_node.previous = self.head.next
        
        new_node.previous.next = new_node.next.previous = new_node
        
    def remove_node(self, value):
        print("Removing node: ")
        current =  self.head.next
        while current is not self.tail:
            if(value is current.value):
                print(f"Found : {value}")
                current.next.previous = current.previous
                current.previous.next = current.next
                return True
            current =  current.next
        return False
        
    def print_forward(self):
        print("Forward: ")
        current =  self.head.next
        
        while current is not self.tail:
            print(current.value)
            current = current.next
            
    def print_backward(self):
        print("Backward: ")
        current = self.tail.previous
        
        while current is not self.head:
            print(current.value)
            current = current.previous
            
            
#run rabit run
slist = Sentinal()
slist.add_to_back("5")
slist.add_to_back("6")
slist.add_to_back("7")

# slist.add_to_front("4")
# slist.add_to_front("3")

slist.print_forward()
slist.remove_node("6")
slist.print_forward()

# slist.print_backward()

        
        