############################################################################
#200. Number of Islands                                                    #
#https://leetcode.com/problems/number-of-islands/                          #
############################################################################

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #4방향 정의
        d_row = [-1,1,0,0]
        d_col = [0,0,-1,1]
        ans = 0
        #깊이 우선 탐색
        def dfs(row,col):
            #현재 노드 방문 처리
            grid[row][col] = '-1'
            for i in range(4):
                n_row = row + d_row[i]
                n_col = col + d_col[i]
                #다음 노드가 grid 범위 안이고 육지이면 계속 탐색
                if 0<= n_row < len(grid) and 0<= n_col <len(grid[0]) and grid[n_row][n_col] == '1':  
                    dfs(n_row,n_col)
            return 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #탐색 안한 육지인 경우 탐색
                if grid[row][col] == '1':
                    ans += dfs(row,col)

        return ans