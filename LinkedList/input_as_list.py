class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class linked_list:
    def create_linked_list(self,my_list):
        if my_list is None:
            return my_list
        head = tail = None
        for item in my_list:
            new_node = Node(item)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
        return head
    
    def middleNode(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sort(self,head):
        if head is None or head.next is None:
            return head
        mid = self.middleNode(head)
        right = mid.next
        left = head
        mid.next = None
        left_sorted = self.sort(left)
        right_sorted = self.sort(right)
        return self.merge(left_sorted, right_sorted)
        
    def print(self):
        if head is None:
            return None
        temp = head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def merge(left,right):
        
        
        
        
        
        
        
        
        
my_list = [10,1,60,30,5]
my_linked_list = linked_list()
head = my_linked_list.create_linked_list(my_list)
my_linked_list.sort(head)
my_linked_list.print()
