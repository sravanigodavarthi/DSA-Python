# def sum_numbers(list1):
#     sum_items = 0
#     for item in list1:
#         sum_items += item
#     return sum_items

# print(sum_numbers([1,2,3,4]))


def sum_numbers(list1):
    if len(list1) == 0:
        return 0
    return list1[0] + sum_numbers(list1[1:])
        
print(sum_numbers([1,2,3,4]))

# - o(n2) time-compleaxity and o(n2) space-complexity