class Solution:
    def reverse_arr(self, arr):
        i = 0 
        j = len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr
    
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int,input().strip().split()))
        print(arr)
        ob = Solution()
        ob.reverse_arr(arr)
        for x in arr:
            print(x,end=' ')
        print()
        tc -= 1
