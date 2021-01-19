class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def dfs(row,col):
            grid[row][col] = 1
            d_row = [-1,1,0,0]
            d_col = [0,0,-1,1]
            
            for i in range(4):
                n_row = row + d_row[i]
                n_col = col + d_col[i]
                
                if 0<=n_row<len(grid) and 0<=n_col<len(grid[0]) and grid[n_row][n_col] == 0:
                    dfs(n_row,n_col)
                    
            return 1

        for row in range(len(grid)):
            if grid[row][0] == 0:
                dfs(row,0)
            if grid[row][len(grid[0])-1] == 0:
                dfs(row,len(grid[0])-1)
        
            
        for col in range(len(grid[0])):
            if grid[len(grid)-1][col] == 0:
                dfs(len(grid)-1,col)
            if grid[0][col] == 0:
                dfs(0,col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    ans += dfs(row,col)
                    
        return ans