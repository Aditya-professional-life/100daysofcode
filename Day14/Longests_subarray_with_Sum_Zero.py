class Solution:
    def maxLen(self, n, arr):

        mpp = {}
        maxi = 0
        
        sum = 0
        for i in range(n):
            sum+=arr[i]
            if sum ==0:
                maxi = i+1
            else:
                if sum in mpp:
                    maxi = max(maxi, i-mpp[sum])
                    
                else:
                    mpp[sum] = i
        return maxi
