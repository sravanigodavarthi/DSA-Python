# Find the Most Frequent Element in a List

# [1,2,3,4,5,6,7,1,2]
# 1 - 2 -> ?
# 2 - 2 -> ?
# Assume: [1,2] -> out
# [1,2,3,4,5,6,7,1,2,3,3,3]
# 3 - 3 -> out
# [1,2,3,4,5,6,7]
# Assume: None?

# intial_count = 0
# {1:2, 2:2, 3:1, 4:1 ..}
# value >= initial_count:
#     most_frequent_element = [most_frequent_element].append(key)
#     initial_count = value 


def most_frequent_element(input_list: list) -> list:
    element_count = {} 
    initial_count = 2
    most_frequent_elements = []
    
    for item in input_list:
        if item in element_count:
            element_count[item] = element_count[item] + 1
        else:
            element_count[item] = 1
     
    for key,value in element_count.items():
        if value >= initial_count:
            most_frequent_elements.append(key)
            initial_count = value
    return most_frequent_elements if most_frequent_elements else None

input_list = [1,2,3,4,5,6,7]
print(most_frequent_element(input_list))


