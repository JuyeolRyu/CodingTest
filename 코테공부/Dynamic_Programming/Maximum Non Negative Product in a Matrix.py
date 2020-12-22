############################################################################
#1594. Maximum Non Negative Product in a Matrix                            #
#https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/   #
############################################################################
#sol1 dfs ==> Time Limit Exceeded
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        d_row = [1,0]
        d_col = [0,1]
        ans = []
        def dfs(row,col,num):
            #끝에 도달
            if row == len(grid)-1 and col == len(grid[0])-1:
                ans.append(grid[row][col] * num)
                return;
            for i in range(2):
                n_row = row + d_row[i]
                n_col = col + d_col[i]
                
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                    dfs(n_row,n_col,num*grid[row][col])
                    
            return;
        
        dfs(0,0,1)
        
        ans = max(ans)
        if ans < 0:
            return -1
        return ans%(10 ** 9 + 7)

#sol2 dynamic programming
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp_max = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp_min = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]
        
        for row in range(1, len(grid)):
            dp_max[row][0] = grid[row][0] * dp_max[row-1][0]
            dp_min[row][0] = grid[row][0] * dp_max[row-1][0]
        for col in range(1, len(grid[0])):
            dp_max[0][col] = grid[0][col] * dp_max[0][col-1]
            dp_min[0][col] = grid[0][col] * dp_max[0][col-1]
        
        for row in range(1,len(grid)):
            for col in range(1,len(grid[0])):
                dp_max[row][col] = max(dp_max[row-1][col]*grid[row][col], dp_max[row][col-1]*grid[row][col],dp_min[row-1][col]*grid[row][col], dp_min[row][col-1]*grid[row][col])
                dp_min[row][col] = min(dp_max[row-1][col]*grid[row][col], dp_max[row][col-1]*grid[row][col],dp_min[row-1][col]*grid[row][col], dp_min[row][col-1]*grid[row][col])

        ans = dp_max[-1][-1]
        if ans < 0:
            return -1
        return ans % (10**9+7)