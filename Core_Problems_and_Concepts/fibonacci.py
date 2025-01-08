# def fibonacci(n):
#     list1 = [0,1]
#     for i in range(n-1):
#         next_sum = list1[i] + list1[i+1]
#         list1.append(next_sum)
    
#     return list1[n]
    
    
# print(fibonacci(35))

#Recursive

def fib(n):
    my_dict = {}
    
    def sum_fib(n):
        
        if n in my_dict:
            return my_dict[n]
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1

        my_dict[n] = sum_fib(n-1) + sum_fib(n-2)
        
        return my_dict[n]
    
    return sum_fib(n)

    
print(fib(6))
