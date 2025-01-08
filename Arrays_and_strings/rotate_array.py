def rotate_array(arr,d):
    # while d > 0:
    #     removed_element = num.pop(0)
    #     num.append(removed_element)
    #     d -= 1
    # return num
    def reverse_array(l,r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l,r = l+1, r-1
            
    rotate_count = d % len(arr)
    reverse_array(0,len(arr)-1)

    reverse_array(0,len(arr)-rotate_count-1)

    reverse_array(len(arr)-rotate_count,len(arr)-1)

    
    return arr 

    
        
        
print(rotate_array([7, 3, 9, 1],9))


