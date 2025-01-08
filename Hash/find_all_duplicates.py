# print ( find_duplicates([1, 2, 3, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 3]) )
# print ( find_duplicates([1, 1, 1, 1, 1]) )
# print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([]) )

def find_duplicates(my_list):
    my_dict = {}
    out = []
    for i in my_list:
        if i in my_dict:
            my_dict[i] = my_dict[i] + 1
        else:
            my_dict[i] = 1
    for key,value in my_dict.items():
        if value > 1:
            out.append(key)
    return out
    
    


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )