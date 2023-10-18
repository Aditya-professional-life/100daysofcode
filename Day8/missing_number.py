
class Solution:
    def missingNumber(self,arr,n):
        sum = 0
        for i in arr:
            sum+=i
        # code here
        return int(((n+1)*n)/2- sum)