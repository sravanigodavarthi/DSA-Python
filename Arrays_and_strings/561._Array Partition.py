# Count Sort
# [4, 2, 2, 8, 3, 3, 1]
def count_sort(arr):
    
    def max_element(arr):
        max = float('-inf')
        for item in arr:
            if item > max:
                max = item
        return max

    def min_element(arr):
        min = float('inf')
        for item in arr:
            if item < min:
                min = item
        return min
    
    max = max_element(arr)
    min = min_element(arr)
    
    count_array = [0] * (max - min +  1)
    
    final_array = [0] * len(arr)
    
    for item in arr:
        count_array[item - min] += 1

    for i in range(0,len(count_array)):
        if i != 0:
            count_array[i] = count_array[i] + count_array[i-1]

    for i in range(len(arr)-1,-1,-1):
        item = arr[i]
        index = count_array[item - min] - 1
        count_array[item-min] -= 1
        final_array[index] = item
    return final_array

def array_partition(s_arr):
    sum = 0
    for i in range(0,len(s_arr),2):
        sum += s_arr[i]
    return sum
        

sorted_array = count_sort([1,4,3,2])
print(array_partition(sorted_array))

# Time & space complexity is o(n+k) and o(n+k)
# Best for small range if integers
# eg: ExamMarks, Ageragne(0-100), sorting colors for image processing, product quantities
# [6,2,6,5,1,2] - 9
