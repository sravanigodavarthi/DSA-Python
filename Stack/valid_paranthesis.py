# str = "((()))" 
# if len(str)%2 == 0:
#     mid = len(str)//2
#     print(mid)
#     left = []
#     right = []
#     for i in range(mid):
#         left.append(str[i])
#     for i in range(mid,len(str)):
#         right.append(str[i])
    
#Stack approach

class Stack:
    def __init__(self):
        self.stack_list = []
        self.matching_parenthesis = {')':'(', ']':'[', '}':'{'}
        
    def push(self,value):
        self.stack_list.append(value)
        
    def pop(self):
        if not self.stack_list:
            return None
        else:
            return self.stack_list.pop()
        
    def valid_paranthesis(self, s):
        for char in s:
            if char in self.matching_parenthesis.values():
                self.push(char)
            elif char in self.matching_parenthesis.keys():
                if not self.stack_list or self.pop() != self.matching_parenthesis[char]:
                    return False
        return len(self.stack_list) == 0
    
    def reverse_string(self,s):
        for char in s:
            self.push(char)
        reverse_string = ""
        while self.stack_list:
            reverse_string += self.pop()
        return reverse_string
        
my_stack = Stack()
print(my_stack.valid_paranthesis("()[]{}"))
print(my_stack.reverse_string("sravani"))