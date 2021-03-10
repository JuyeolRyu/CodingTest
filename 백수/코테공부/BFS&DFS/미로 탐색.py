#https://www.acmicpc.net/problem/2178
import sys
from collections import deque
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
grid = [list(map(int,input())) for i in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(row,col):
  q = deque()
  q.append([0,0])

  while q:
    r,c = q.popleft()

    for i in range(4):
      nr = r+dr[i]
      nc = c+dc[i]

      if 0<= nr < n and 0<= nc < m and grid[nr][nc] == 1:
        grid[nr][nc] += grid[r][c]
        q.append([nr,nc])

bfs(0,0)
print(grid[-1][-1])