# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        ans = 0
        for j in  range(1,m):
            for i in range(n):
                mx= float('-inf')
                
                if i-1 >=0 and j-1>=0:
                    mx= max(mx,M[i-1][j-1])
                    
                if j-1>=0:
                    mx = max(mx,M[i][j-1])
                    
                    
                if i+1 <n and j-1>=0:
                    mx= max(mx,M[i+1][j-1])
                    
                M[i][j] +=mx
                
                ans = max(ans,M[i][j])
                
        return ans

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends