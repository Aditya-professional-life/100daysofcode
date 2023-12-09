#User function Template for python3
class Solution:
    def sumdigit(self, x):
        sum = 0
        while x:
            sum += x % 10
            x = x // 10
        return sum

    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def smithNum(self, n):
        sum = self.sumdigit(n)
        sum2 = 0

        if self.isPrime(n):
            return 0

        for i in range(2, n):
            if n % i == 0:
                s = self.sumdigit(i)
                while n > 0 and n % i == 0:
                    sum2 += s
                    n = n // i

        if sum == sum2:
            return 1
        return 0

# 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends