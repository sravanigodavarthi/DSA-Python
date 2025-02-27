# Reverse a string without using reverse function

# Reversing a string in-place with O(1) space is not possible in Python due to the immutable nature of strings.
# Thus, O(1) space complexity is not achievable for string reversal in Python

# def reverse_string(my_string):
#     out = my_string[::-1]
#     return out
# print(reverse_string('sravani'))

# time complexity & space complexity o(n)
# While slicing is a more efficient operation compared to concatenation 
# (because it doesn't require copying the whole string multiple times), 
#  it still involves copying the characters from the original string to create a new string.


def rev_str(input):
    reversed_str = []
    for i in range(len(input)-1,-1,-1):
       reversed_str.append(input[i])
    return ''.join(reversed_str)
print(rev_str("sravani"))
    
# time complexity & space complexity o(n)
# The join() method is O(n), where n is the number of elements in the list. 
# This operation concatenates all the elements of the list into a single string in a single pass



# def rev_str(input):
#     reversed_str = ""
#     for i in range(len(input)-1,-1,-1):
#        reversed_str = reversed_str + input[i]
#     return reversed_str
# print(rev_str("sravani"))

# time complexity o(n^2) & space complexity o(n)
# When you concatenate two strings, Python needs to allocate new memory for the result 
# and copy the characters from both strings into it.