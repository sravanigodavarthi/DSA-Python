def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        return create_dict(str1) == create_dict(str2)
    
def create_dict(s):
    my_dict = {}
    for char in s:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict



print(anagram('restful', 'fluster'))
print(anagram('cats', 'tocs'))
print(anagram('monkeyswrite', 'newyorktimes'))
print(anagram('paper', 'reapa'))