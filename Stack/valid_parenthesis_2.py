# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

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
        
    def push(self,value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value 

    def valid_paranthesis(self,s):
        my_dict = {']':'[','}':'{',')':'('}
        for char in s:
            if char in my_dict.values():
                self.push(char)
            else:
                if self.top is None or self.pop() != my_dict[char]:
                    return False
        return self.top is None
                
    
my_stack = Stack()
print(my_stack.valid_paranthesis('([][{}}])'))