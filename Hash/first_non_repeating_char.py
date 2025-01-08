def first_non_repeating_char(str):
    my_dict = {}
    for i in str:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
            
    for key,value in my_dict.items():
        if value == 1:
            return key
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbc') )
