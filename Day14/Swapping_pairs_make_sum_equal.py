class Solution:
    def binary_search(self,arr,target):
        
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def findSwapValues(self,a, n, b, m):
        a.sort()
        b.sort()

        sum1, sum2 = sum(a), sum(b)

        if (sum1 + sum2) % 2 != 0:
            return -1

        avg = (sum1 + sum2) // 2
        diff = avg - min(sum1, sum2)

        for i in range(n):
            if self.binary_search(b, i + diff) or self.binary_search(b, -(i + diff)):
                return 1

        return -1
            

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends