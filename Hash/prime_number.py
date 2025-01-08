# 1.⁠ ⁠Write a function to that takes a list of integers and return a new list containing only prime numbers.

# A prime number must have exactly two distinct positive divisors:
# The number 1 itself
# The number

# Iterate from 2 to the square root of n:
# We only need to check for divisibility up to the square root of n 
# because if a number has a divisor greater than its square root, 
# it also has a divisor smaller than its square root.

# [1,2,3,4,5,6,7]

def prime_number(nums):
    out = []
    for item in nums:
        if item == 2:
            out.append(item)
        elif item > 1:
            is_prime = 1
            for i in range(2, int(item**0.5)+1):
                if item % i == 0:
                    is_prime = 0
                    break
            if is_prime == 1:
                out.append(item)
    return out

print(prime_number([1,2,3,4,5,6,7,9,15]))


# time complexity: o(n*squareroot(m)), m is the largest number in the list