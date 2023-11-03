class Solution:

	def checkTriplet(self,arr, n):
    	# code here
        hash_map = {}
        for i in arr:
            hash_map[i * i] = i
        
        for i in hash_map:
            for j in hash_map:
                sum = i+j
                
                if sum in hash_map:
                    return True
            
        return False