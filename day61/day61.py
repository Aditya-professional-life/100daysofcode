#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        window = float('inf')
        zero, one, two = -1, -1, -1

        for i in range(len(S)):
            if S[i] == '1':
                one = i
            elif S[i] == '0':
                zero = i
            else:
                two = i

            if zero != -1 and one != -1 and two != -1:
                mini = min(zero, one, two)
                maxi = max(zero, one, two)
                window = min(window, maxi - mini + 1)

        if window == float('inf'):
            return -1
        else:
            return window
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends