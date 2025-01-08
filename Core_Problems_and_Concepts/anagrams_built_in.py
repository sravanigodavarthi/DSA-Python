from collections import Counter

def anagram(str1,str2):
    count = Counter(str1)
    print(count['e'])
    return Counter(str1) == Counter(str2)

print(anagram('restful', 'fluster'))
print(anagram('cats', 'tocs'))
print(anagram('monkeyswrite', 'newyorktimes'))
print(anagram('paper', 'reapa'))