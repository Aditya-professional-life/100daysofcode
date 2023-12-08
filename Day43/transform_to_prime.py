#User function Template for python3



class Solution:
    def isprime(self, x):
        if x == 1:
            return False
        if x == 2:
            return True
        root = int(x**0.5)
        for i in range(2, root + 1):
            if x % i == 0:
                return False
        return True

    def minNumber(self, arr, n):
        # code here
        if sum(arr) ==1:
            return 1
        array_sum = sum(arr)
        if self.isprime(array_sum):
            return 0

        for i in range(array_sum + 1, 2 * array_sum):
            if self.isprime(i):
                return i - array_sum

        return 0




#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends