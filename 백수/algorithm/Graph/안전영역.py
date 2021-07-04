#https://www.acmicpc.net/problem/2468
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
'''
def dfs(r,c,h):
  for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]
    if 0<=nr<N and 0<=nc<N:
      if grid[nr][nc] > h and not visited[nr][nc]:
        visited[nr][nc] = True
        dfs(nr,nc,h)
  return 1
'''
def bfs(r,c):
  q = deque()
  q.append([r,c])
  visited[r][c] = True

  while q:
    r,c = q.popleft()
    for i in range(4):
      nr = r+dr[i]
      nc = c+dc[i]
      if 0<=nr<N and 0<=nc<N:
        if grid[nr][nc] > h and not visited[nr][nc]:
          visited[nr][nc] = True
          q.append([nr,nc])
  return 1

#Value
dr = [-1,1,0,0]
dc = [0,0,-1,1]
maxH = 0
ans = 0
#input
N = int(input())
grid = []
for i in range(N):
  tmp = list(map(int,input().split()))
  maxH = max(tmp+[maxH])
  grid.append(tmp)

for h in range(maxH+1):
  ret = 0
  visited = [[False]*N for _ in range(N)]
  for row in range(N):
    for col in range(N):
      if grid[row][col] > h and not visited[row][col]:
        visited[row][col] = True
        ret += bfs(row,col)
  ans = max(ret,ans)
  

print(ans)