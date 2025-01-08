
# My solution it works but there is no proper mechanism followed

# class Solution:
#     def pushZerosToEnd(self, arr):
#         # code here
#         i = 0
#         j = 0
#         while j < len(arr):
#             if arr[i] != 0 and arr[j] != 0:
#                 i += 1
#                 j += 1
#             elif arr[i] == 0 and arr[j] == 0:
#                 j += 1
#             elif arr[i] == 0 and arr[j] != 0:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 i += 1
#                 j += 1
#         return arr

# Solution by greeksforgreeks

class Solution:
    def pushZerosToEnd(self, arr):
        # code here
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i],arr[count] = arr[count],arr[i]
                count += 1
        return arr

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

