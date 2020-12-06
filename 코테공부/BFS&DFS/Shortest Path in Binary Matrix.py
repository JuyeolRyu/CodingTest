############################################################################
#1091. Shortest Path in Binary Matrix                                      #
#https://leetcode.com/problems/shortest-path-in-binary-matrix/             #
############################################################################
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #시작하거나 끝낼수 없는 경우 -1 반환
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        #시작과 끝이 같은 경우
        if len(grid) == 1 and len(grid[0]) == 1:
            return 1
        
        #큐 생성
        queue = deque()
        queue.append([0,0])
        #상하좌우대각선 방향 저장 리스트
        d_row = [-1,1,0,0,-1,-1,1,1]
        d_col = [0,0,-1,1,1,-1,-1,1]
        #큐에 값이 있을때만 반복
        while queue:
            row, col = queue.popleft()
            #끝지점 까지 가지못할 경우를 위해 예외처리
            if row == len(grid)-1 and col == len(grid)-1:
                break
            #모든방향 순회
            for i in range(8):
                n_row = row + d_row[i]
                n_col = col + d_col[i]
                #다음 칸이 갈수 있을 경우만 전진
                if 0<=n_row<len(grid) and 0<=n_col<len(grid):
                    if grid[n_row][n_col] == 0:
                        grid[n_row][n_col] = grid[row][col] +1
                        queue.append([n_row,n_col])
        #도착 못한 경우
        if grid[-1][-1] == 0:
            return -1
        return grid[-1][-1]+1