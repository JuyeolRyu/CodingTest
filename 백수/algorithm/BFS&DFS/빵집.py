#https://www.acmicpc.net/problem/3109
#빵집 3109
r,c = map(int,input().split())
grid = []
d_row = [-1,0,1]
for i in range(r):
  grid.append(list(input()))

def dfs(row,col):
  if col == c-1:
    return True

  for i in range(3):
    n_row = row + d_row[i]
    n_col = col + 1

    if 0<=n_row<r and 0<=n_col<c and grid[n_row][n_col] != 'x':
      grid[n_row][n_col] = 'x'
      if dfs(n_row,n_col):
        return True

  return False

ans = 0
for row in range(r):
  if dfs(row,0):
    ans += 1

print(ans)