def max_value(list1):
    max = float('-inf')
    for num in list1:
        if num > max:
            max = num
    return max

list1 = [-1,-5,-7,-9,-2]
print(max_value(list1))
