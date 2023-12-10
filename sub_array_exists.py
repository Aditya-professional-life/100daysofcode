#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        hash_map = {}
    
        for i in range(n):
            if arr[i] == 0:
                return True
        
        ans = False
        _sum = 0
        for i in range(n):
            _sum += arr[i]
            
            if _sum in hash_map or _sum == 0:
                ans = True
                break
            
            hash_map[_sum] = hash_map.get(_sum, 0) + 1
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends