# Write a program to find the total number of anagrams in a list
# anagrams: total number to chars in a word irrespective of the order. 
# If two words has same characters and occurance irrespective of the order.

# Input: ['atr','inch','eat','tac','tea','cat','chin']

# output: (ate,eat,tea),(cat,tac),(inch,chin)


# 1. Create a hash key logic that groups the anagrams -> out is an dict with hashvalue as key(tuple) and words as values(list)
# 2. to count total number of anagram, loop to the out dict and if len(values) > 1 than count+


def create_hash_key(word: str) -> str:
    hash_key = [0]*26
    for char in word.lower():
        hash_key[ord(char) - ord('a')] += 1
    return(tuple(hash_key))
    
def total_anagrams(input: list) -> int:
    anagram_dict = {}
    for word in input:
        key = create_hash_key(word)
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]
    count = 0
    anagram_groups = []
    for key, value in anagram_dict.items():
        if len(value) > 1:
            count += 1
            anagram_groups.append(value)
    return(count,anagram_groups)
    
print(total_anagrams(['ate','inch','eat','tac','tea','cat','chin']))