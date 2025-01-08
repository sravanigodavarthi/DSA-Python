# def intersection(list1,list2):
#     result = []
#     items = set()
#     for item in list1:
#         items.add(item)
#     for item in list2:
#         if item in items:
#             result.append(item)
#     return result

def intersection(list1,list2):
    items_set = set(list1)
    return [item for item in list2 if item in items_set]
print(intersection([4,2,1,6], [3,6,9,2,10]))