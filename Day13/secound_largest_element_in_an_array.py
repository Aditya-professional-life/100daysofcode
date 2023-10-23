	def print2largest(self,arr, n):
        max1 = max2 = float('-inf')
        
        for x in arr:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2 and x != max1:
                max2 = x
        
        if max2 == float('-inf'):
            return -1
        return max2
