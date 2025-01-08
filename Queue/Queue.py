class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next    
                
    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.first.next is None:
            self.first = None
            self.last = None
            return temp.value
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        return temp.value
        
my_queue = Queue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
my_queue.enqueue(9)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
# last_value = my_queue.dequeue()
# print(f"remove value is {last_value}")
my_queue.print_queue()