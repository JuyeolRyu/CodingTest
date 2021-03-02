#https://www.acmicpc.net/problem/1520
r,c=map(int,input().split())
grid = []
dp = [[-1 for i in range(c)] for j in range(r)]

for i in range(r):
  grid.append(list(map(int,input().split())))

def find_road(row,col):
  if row == r-1 and col == c-1:
    return 1
  if dp[row][col] != -1:
    return dp[row][col]
  dp[row][col] = 0
  d_row = [-1,1,0,0]
  d_col = [0,0,-1,1]

  for i in range(4):
    n_row = row+d_row[i]
    n_col = col+d_col[i]

    if 0<=n_row<r and 0<=n_col<c and grid[row][col] > grid[n_row][n_col]:
      dp[row][col] += find_road(n_row,n_col)

  return dp[row][col]

find_road(0,0)
print(dp[0][0])
for row in dp:
  print(row)
'''
4 5
50 45 37 32 30
35 2 1 20 25
30 30 25 17 28
27 24 22 15 10
'''