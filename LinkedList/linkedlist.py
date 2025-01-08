# head = {'value' : 11, 
#             'next' :{'value' : 3,
#             'next': {'value': 23,
#             'next' : {'value': 7,
#             'next' : None
#              }
#             }
#             }
#             }
# print(head['value'])
# print(head['next']['value'])
# print(head['next']['next']['value'])

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
        
# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
    
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
        
#     def append(self,value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

# my_linkedlist = LinkedList(4)
# my_linkedlist.append(2)
# my_linkedlist.print_list()
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
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            
    def remove(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
my_linkedlist = LinkedList(2)
my_linkedlist.append(4)
my_linkedlist.append(5)
my_linkedlist.append(6)
my_linkedlist.append(7)
my_linkedlist.remove()
my_linkedlist.append(7)
my_linkedlist.print_list()
