#middle node of a linked list
# 1 2 3 4 5

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
        
my_linkedlist = LinkedList(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.append(5)
my_linkedlist.append(6)
middle_node = my_linkedlist.middle_node()
print(middle_node.value)

