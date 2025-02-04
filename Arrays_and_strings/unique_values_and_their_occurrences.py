# 1. Write a Python script to identify unique values in a list and count their occurrences. 
# This tests your understanding of sets and dictionaries.

from collections import defaultdict

def unique_values_and_occurrence(nums):
    out = {}
    for num in nums:
        if num in out:
            out[num] += 1
        else:
            out[num] = 1
    return out
    
print(unique_values_and_occurrence([1,2,2,3,4,5,5,5,6,7]))
# expected_out: {1:1,2:2,3:1,4:1,}5:3,6:1,7:1}