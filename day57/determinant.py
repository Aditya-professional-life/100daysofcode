class Solution:
    def determinantOfMatrix(self, matrix, n):
        if n == 1:
            return matrix[0][0]

        ans = 0
        for i in range(n):
            inner_mat = [row[:i] + row[i + 1:] for row in matrix[1:]]
            ans += matrix[0][i] * self.determinantOfMatrix(inner_mat, n - 1) * (-1 if i % 2 else 1)

        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends