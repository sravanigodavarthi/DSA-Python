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
    
    def middlenode(self, head):
        mid_prev = None
        while head and head.next:
            mid_prev = head if not mid_prev else mid_prev.next
            head = head.next.next
        mid = mid_prev.next
        mid_prev.next = None
        return mid

    def sort(self,head):
        if head is None or head.next is None:
            return head
        mid = self.middlenode(head)
        left = self.sort(head)
        right = self.sort(mid)
        return self.merge(left, right)
        
    def print(self,head):
        if head is None:
            return None
        temp = head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def merge(self,left,right):
        dummy_head = Node(0)
        tail = dummy_head
        while left and right:
            if left.value < right.value:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy_head.next  

my_list = [10,1,60,30,5]
my_linked_list = linked_list()
head = my_linked_list.create_linked_list(my_list)
sorted_head = my_linked_list.sort(head)
my_linked_list.print(sorted_head)

    