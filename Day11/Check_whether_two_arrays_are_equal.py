
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        hash_map = {}
        for i in range(N):
            if A[i] in hash_map:
                hash_map[A[i]]+=1
            else:
                hash_map[A[i]]=1
                
                
        for i in range(N):
            if B[i] in hash_map:
                hash_map[B[i]]-=1
            else:
                return 0
                break
            
        for i in hash_map.keys():
            if hash_map[i] != 0:
                return 0
            
        return 1
            