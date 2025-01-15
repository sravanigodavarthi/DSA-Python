# Write a function to find all the unique combinations of numbers in a list that add up to a given target.
# Input: nums = [2, 3, 6, 7, 1], target = 7

def unique_combinations(target, nums):
    result = []
    def back_track(total, cur_comb, start):
        if total > target:
            return
        if total == target:
            result.append(list(cur_comb))
            return
        for i in range(start,len(nums)):
            cur_comb.append(nums[i])
            back_track(total+nums[i],cur_comb,i)
            cur_comb.pop()
    
    back_track(0,[],0)
    
    return result

print(unique_combinations(7, [2, 3, 6, 7, 1]))

# The time complexity is O(N^T/S*T/S)
# The space complexity is O(T/S)