# def duplicates_inplace(nums):
#     i = 0
#     j = 1
#     while j < len(nums):
#         if nums[i] == nums[j]:
#             j += 1
#         if nums[i] != nums[j]:
#             nums[i+1] = nums[j]
#             i += 1
#             j += 1 
#     return nums[:i+1], i+1

# def duplicates_inplace(nums):
#     i = 0
#     for j in range(1,len(nums)):
#         if nums[i] != nums[j]:
#             i += 1
#             nums[i] = nums[j]
#     return nums[:i+1], i+1

# def duplicates_inplace(nums):
#     for i in range(len(nums)-1,0,-1):
#         if nums[i] == nums[i-1]:
#             nums.pop(i)
#     return nums, len(nums)
# time complexity o(n)2

print(duplicates_inplace([0,0,1,1,1,2,2,3,3,4]))


