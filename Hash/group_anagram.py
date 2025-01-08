def group_anagrams(my_list):
    my_dict = {}
    for item in my_list:
        key = key_generation(item)
        if key in my_dict:
            my_dict[key] = my_dict[key]+[item]
        else:
            my_dict[key] = [item]
    return list(my_dict.values())
        
def key_generation(str):
    count = [0] * 26
    for char in str:
        count[ord(char) - ord("a")] += 1
    return tuple(count)

# the ASCII value of two str which are not anagram can also be same eg: 'ab' & 'ac' 

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )
