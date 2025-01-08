def sum_possible(list1,target):
    my_dict = {}
    for item in list1:
        diff = target - item
        if diff in my_dict:
            return my_dict[diff]
        my_dict[diff] = True
    return False
        
print(sum_possible([6,4,10], 15))