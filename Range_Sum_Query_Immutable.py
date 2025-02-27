list1 = [1,2,3,4,5]
cumulative_sum = [0] * (len(list1)+1)
for i in range(len(list1)):
    cumulative_sum[i+1] = cumulative_sum[i] + list1[i] 
print(cumulative_sum)