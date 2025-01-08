class Stack:
    def __init__(self):
        self.stack_list = []
    def print_stack(self):
        if not self.stack_list:
            print("list is empty")
        else:
            for i in self.stack_list:
                print(i)
    def push(self,value):
        self.stack_list.append(value)
    def pop(self):
        self.stack_list.pop()
         
my_stack = Stack()
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.push(8)
my_stack.push(9)
my_stack.push(10)
my_stack.pop()
my_stack.pop()
my_stack.print_stack()