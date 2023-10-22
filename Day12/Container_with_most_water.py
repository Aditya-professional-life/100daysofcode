def maxArea(A,le):
    #code here
    left = 0
    right = len(A)-1
    res = 0
    while left  < right:
        area = (right-left)*min(A[left],A[right])
        res = max(area,res)
            
        if A[left] <A[right]:
            left+=1
        else:
            right-=1
        
    return res