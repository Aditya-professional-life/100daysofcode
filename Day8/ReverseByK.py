class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        result=[]
        max_element=A[N-1]
        result.append(max_element)
        for i in range(N-2,-1,-1):
            if max_element<=A[i]:
                result.append(A[i])
                max_element=A[i]
        return result[::-1]

