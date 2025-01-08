# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

class Solution:
    def compress(self, chars: list[str]) -> int:
        r = 0
        i = 0
        while i < len(chars):
            curchar = chars[i]
            curocurr = 0
            while i < len(chars) and curchar == chars[i]:
                curocurr += 1
                i += 1
            chars[r] = curchar
            r += 1
            if curocurr > 1:
                occurstr = str(curocurr)
                for j in occurstr:
                    chars[r] = j
                    r += 1
        return r
    
a = Solution()
chars = ["a", "a", "b", "b", "c"]
length = a.compress(chars)
print(chars[:length])