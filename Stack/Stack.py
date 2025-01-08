class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self,value=None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
        else:
            self.top = None
            
    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next
    
    def Push(self,value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    def Pop(self):
        if self.top == None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
            
my_stack = Stack()
my_stack.Push(5)
my_stack.Push(6)
my_stack.Push(8)
my_stack.Push(7)
my_stack.Pop()
my_stack.Push(7)
# item = my_stack.Pop()
# print(item)
my_stack.print_stack()