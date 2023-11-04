class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        if arr[n-1] == 0:
            return -1
        if arr[0] ==1:
            return 0
        
        low = 0
        high = n-1
        
        while low < high:
            mid = (low+high) //2
            if arr[mid] ==0:
                if arr[mid+1] ==1:
                    return mid+1
                else:
                    low = mid+1
                    
            elif arr[mid]==1:
                if arr[mid-1] ==0:
                    return mid
                else:
                    high = mid -1