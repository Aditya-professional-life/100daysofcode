#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        if K >N:
            return 
        
        s1 = sum(Arr[:K])
        max_sum = s1
        
        for i in range(N-K):
            s1 = s1 - Arr[i]+Arr[i+K]
            max_sum = max(max_sum,s1)
            
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends