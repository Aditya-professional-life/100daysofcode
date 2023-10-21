class Solution:
    def maximumSumSubarray (self,k,arr,n):
        
        if k >n:
            return 
        
        window_sum = sum(arr[:k])
        
        max_sum = window_sum
        
        for i in range(n-k):
            window_sum = window_sum - arr[i] + arr[i+k]
            max_sum = max(max_sum,window_sum)
        
        
        return max_sum