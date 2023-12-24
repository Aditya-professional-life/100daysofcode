

import heapq
from typing import List

class Solution:
    def buyMaximumProducts(self, n: int, k: int, price: List[int]) -> int:
        v = [(price[i], i + 1) for i in range(n)]
        heapq.heapify(v)  # Convert the list to a min-heap

        ans = 0

        while v and k > 0:
            p, count = heapq.heappop(v)
            max_buy = min(k // p, count)
            ans += max_buy
            k -= p * max_buy

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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends