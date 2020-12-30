############################################################################
#1314. Matrix Block Sum                                                    #
#https://leetcode.com/problems/matrix-block-sum/                           #
############################################################################

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n+1) for i in range(m+1)]
        ans = [[0] * n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = mat[i][j]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] +=  dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        
        for row in range(m):
             for col in range(n):
                s_row,e_row = max(0,row-k), min(m,row+k+1)
                s_col,e_col = max(0,col-k), min(n,col+k+1)
                ans[row][col] = dp[e_row][e_col] - dp[s_row][e_col] - dp[e_row][s_col] + dp[s_row][s_col]

        return ans
        