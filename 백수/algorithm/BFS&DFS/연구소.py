#https://www.acmicpc.net/problem/14502

#sol1 combinations & bfs
import sys,copy
from itertools import combinations
from collections import deque

n,m = map(int,sys.stdin.readline().split())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
zero = []
ans = 0
#find Zero
for i in range(n):
  for j in range(m):
    if grid[i][j] == 0:
      zero.append([i,j])


def bfs(row,col):
  dr = [-1,1,0,0]
  dc = [0,0,-1,1]
  
  cnt = 1
  q = deque()
  q.append([row,col])

  while q:
    r,c = q.popleft()
    for i in range(4):
      nr = r+dr[i]
      nc = c+dc[i]

      if 0<=nr<n and 0<=nc<m and visited[nr][nc] == 0:
        visited[nr][nc] = 2
        q.append([nr,nc])

  return cnt

for comb in list(combinations(zero,3)):
  tmp = 0
  visited = copy.deepcopy(grid)
  visited[comb[0][0]][comb[0][1]] = 1
  visited[comb[1][0]][comb[1][1]] = 1
  visited[comb[2][0]][comb[2][1]] = 1
  
  for i in range(n):
    for j in range(m):
      if visited[i][j] == 2:
        bfs(i,j)
  for row in visited:
    tmp += row.count(0)
  ans = max(ans,tmp)

print(ans)


#sol2 bfs & 벽 찾아가면서 풀기
import sys

from collections import deque
n,m = map(int,sys.stdin.readline().split())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = 0

def bfs():
  global ans
  ret = 0
  dr = [-1,1,0,0]
  dc = [0,0,-1,1]
  copy_grid = [[0 for i in range(m)] for j in range(n)]

  for i in range(n):
    for j in range(m):
      copy_grid[i][j] = grid[i][j]

  for i in range(n):
    for j in range(m):
      if copy_grid[i][j] == 2:
        q.append([i,j])

  while q:
    r,c = q.popleft()
    for i in range(4):
      nr = r+dr[i]
      nc = c+dc[i]

      if 0<=nr<n and 0<=nc<m and copy_grid[nr][nc] == 0:
        copy_grid[nr][nc] = 2
        q.append([nr,nc])
  
  for row in copy_grid:
    ret += row.count(0)
  ans = max(ans,ret)

def wall(x):
  if x== 3:
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 0:
        grid[i][j] = 1
        wall(x+1)
        grid[i][j] = 0

q = deque()
wall(0)
print(ans)