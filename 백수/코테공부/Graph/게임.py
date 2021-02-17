import sys
import copy
sys.setrecursionlimit(100000)
n,m = map(int,input().split())
grid = []
visited = []

dp = []
for _ in range(n):
  grid.append(list(input()))
  visited.append([False for i in range(m)])
  dp.append([0 for i in range(m)])
finished = copy.deepcopy(visited)
def isCycle(row,col):
  if visited[row][col]:
    return True
  visited[row][col] = True
  
  ret = False
  d_row = [-1,1,0,0]
  d_col = [0,0,-1,1]

  for i in range(4):
    n_row = row+d_row[i]*int(grid[row][col])
    n_col = col+d_col[i]*int(grid[row][col])

    if 0<=n_row<n and 0<=n_col<m and grid[n_row][n_col] != 'H' and not finished[n_row][n_col]:
      ret = ret or isCycle(n_row,n_col)
  visited[row][col] = False
  finished[row][col] = True
  return ret

def dfs(row,col):
  if row<0 or row>=n or col<0 or col>=m or grid[row][col] == 'H':
    return 0
  if dp[row][col] != 0:
    return dp[row][col]
  
  dp[row][col] = 1

  d_row = [-1,1,0,0]
  d_col = [0,0,-1,1]

  for i in range(4):
    n_row = row+d_row[i]*int(grid[row][col])
    n_col = col+d_col[i]*int(grid[row][col])
    dp[row][col] = max(dp[row][col],dfs(n_row,n_col)+1)
  return dp[row][col]
if isCycle(0,0):
  print(-1)
else:
  print(dfs(0,0))