#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
		mod = 1e9+7
		if n==1:
		    return 1
		if n==2:
		    return 2
		f =1
		s =2
		
		for i in range(3,n+1,1):
		    t = (f+s)%mod
		    f=s
		    s=t
		    
		    
		return int(s)
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends