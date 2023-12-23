#User function Template for python3


class Solution:
    
    def countOccurence(self, arr, n, k):
        count = n / k

        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        ans = 0
        for i in hash_map.keys():
            if hash_map[i] >count:
                ans += 1

        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends