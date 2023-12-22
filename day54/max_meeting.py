from typing import List

class Solution:
    def maxMeetings(self, N, S, F):

        v = [(F[i], S[i], i + 1) for i in range(N)]

        v.sort()

        ans = []
        end = v[0][0]
        ans.append(v[0][2])

        for i in range(1, N):
            if v[i][1] > end:
                ans.append(v[i][2])
                end = v[i][0]

        ans.sort()
        return ans


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends