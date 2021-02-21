#https://www.acmicpc.net/problem/4963
#섬의 개수 4963
d_row = [-1,-1,-1,0,0,1,1,1]
d_col = [-1,0,1,-1,1,-1,0,1]
while True:
  c,r = map(int,input().split())
  if c == 0 and r == 0:
    break
  grid = []
  
  for i in range(r):
    grid.append(list(map(int,input().split())))

  def dfs(row,col):
    if row<0 or row>=r or col<0 or col>=c or grid[row][col] != 1:
      return;
    #방문한 땅 표시
    grid[row][col] = 2
    for i in range(8):
      n_row = row+d_row[i]
      n_col = col+d_col[i]
      dfs(n_row,n_col)
    return;
  ans = 0
  for row in range(r):
    for col in range(c):
      if(grid[row][col] == 1):
        dfs(row,col)
        ans += 1

  print(ans)