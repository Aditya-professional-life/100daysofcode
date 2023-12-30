#User function Template for python3

class Solution:
    def winner(self,arr, n):
        vote_count = {}
        for candidate in arr:
            vote_count[candidate] = vote_count.get(candidate, 0) + 1
    
        winner_candidate = ""
        max_votes = 0
    
        for candidate, votes in vote_count.items():
            if votes > max_votes or (candidate < winner_candidate and votes == max_votes):
                max_votes = votes
                winner_candidate = candidate
    
        return [winner_candidate, str(max_votes)]    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends