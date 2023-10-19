class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        last_idx = n - 1
        first_idx = 0
        maxi = arr[n - 1] + 1
        
        for i in range(n):
            if i % 2 == 0:
                arr[i] += (arr[last_idx] % maxi) * maxi
                last_idx -= 1
            else:
                arr[i] += (arr[first_idx] % maxi) * maxi
                first_idx += 1
    
        for i in range(n):
            arr[i] //= maxi
