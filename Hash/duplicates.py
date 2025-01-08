# you have a list1=[1,2,2,4,5,6,7,7,20,20]
# Find out the duplicate element from the list and store it in another list.

def duplicate_list(my_list):   
    count_dict = {}
    out_list = []
    for item in my_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
            
    for key,value in count_dict.items():
        if value > 1:
           out_list.append(key)
    return out_list

list1=[1,2,2,4,5,6,7,7,20,20]
print(duplicate_list(list1))