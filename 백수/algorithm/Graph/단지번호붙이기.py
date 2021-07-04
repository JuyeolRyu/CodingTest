#https://www.acmicpc.net/problem/1541
import sys
input = sys.stdin.readline
def dfs(r,c):
  ret = 1
  grid[r][c] = 2
  for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]
    if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 1:
      ret += dfs(nr,nc)
  return ret
dr = [-1,1,0,0]
dc = [0,0,-1,1]
n = int(input())
grid = []
visited = []
ans = []
ans_n = 0
for _ in range(n):
  grid.append(list(map(int,input().rstrip())))

for row in range(n):
  for col in range(n):
    if grid[row][col] == 1:
      ans.append(dfs(row,col))
      ans_n += 1

ans = sorted(ans)
print(ans_n)
for a in ans:
  print(a)
