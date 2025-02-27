# Find the Missing Number in an Array

#  The array may contain all the numbers except for one from a consecutive sequence.

# [1,2,3,5,6] -> out 4
# None

def missing_number(arr):
    for i in range(0,len(arr) - 1):
        if arr[i+1] - arr[i] != 1:
            return arr[i] + 1
    return None

arr = [1,2,3,4,5]
print(missing_number(arr))