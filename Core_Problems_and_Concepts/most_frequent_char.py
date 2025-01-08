def char_occurance(s):
    count = {}
    max_count = 0
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for key,value in count.items():
        if value > max_count:
            max_count = value
            most_frequent_char = key
    return most_frequent_char
    
print(char_occurance('bookeeper'))
print(char_occurance('david'))
print(char_occurance('abby'))
print(char_occurance('mississippi'))