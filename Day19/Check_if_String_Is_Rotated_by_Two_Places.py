class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,s1,s2):
        if len(s1) != len(s2):
            return 0
        
        right = s1[-2:] +s1[:-2]
        left = s1[2:] + s1[:2]
        
        
        return 1 if s2 ==right or s2==left else 0
        #code here