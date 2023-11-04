def solveMem(n,x,y,z,dp):
    #basecase
    if(n==0):
        return 0
    if(n<0):
        return float('-inf')
    
    if(dp[n]!=-1):
        return dp[n]
    
    a = solveMem(n-x,x,y,z,dp)+1
    b = solveMem(n-y,x,y,z,dp)+1
    c = solveMem(n-z,x,y,z,dp)+1
    
    dp[n] = max(a,max(b,c))
    return dp[n]
                     


def cutSegments(n, x, y, z):
    dp = []
    for i in range(n+1):
        dp.append(-1)
    ans = solveMem(n,x,y,z,dp)
    if ans<0:
        return 0
    else:
        return ans