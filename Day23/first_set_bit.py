
class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):        
        res = 0
        while n > 0:
            if n % 2 == 1:
                return res + 1
            n = n // 2
            res += 1
        return 0  