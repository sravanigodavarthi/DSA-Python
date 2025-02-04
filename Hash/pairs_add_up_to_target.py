# Find the pairs that add up-to a target 
# Input - [1,2,3,4],5
# Output - [[2,3],[1,4]]


# Cosidering no negative numbers and also no duplicates:
#     1. I will create empty dict and push items to dict if diff is not in dict
#     2. if diff in dict I will get the key and diff and append to list
    
    
def pairs_adds_to_target(input: list,target: int) -> list:
    input_set = set()
    pairs_list = []
    for item in input:
        diff = target - item
        if diff in input_set:
             pairs_list.append([diff,item])
        input_set.add(item)
    return pairs_list

print(pairs_adds_to_target([1,2,3,4],5))

# Handling Negative Numbers and Duplicates


def pairs_adds_to_target_2(input: list,target: int) -> list:
    input_dict = set()
    pairs_set = set()
    pairs_list = []
    for item in input:
        diff = target - item
        if diff in input_dict:
             pair = tuple(sorted([diff,item]))
             if pair not in pairs_set:
                pairs_list.append([diff,item])
                pairs_set.add(pair)
        input_dict.add(item)
    return pairs_list

print(pairs_adds_to_target([1,2,3,4],5))