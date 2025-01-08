
# HT: Subarray Sum ( ** Interview Question)
# Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

# Your function should take two arguments:

# nums: a list of integers representing the input array

# target: an integer representing the target sum

# nums = [1, 2, 3, 4, 5]
# target = 9
# print(subarray_sum(nums, target))  # should print [1, 3]

def subarray_sum(my_list,target):
    my_dict = {0:-1}
    current_sum = 0
    for index,value in enumerate(my_list):
        current_sum += value
        if current_sum - target in my_dict:
            print(my_dict)
            return [my_dict[current_sum - target]+1,index]
        my_dict[current_sum] = index
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )