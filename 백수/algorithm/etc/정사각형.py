#https://www.acmicpc.net/problem/1051

n,m = map(int,input().split())
grid = []
ans = 0
for i in range(n):
  grid.append(list(input()))

def isSquare(row,col):
  i = 1
  ret = 0
  while True:
    if row+i < 0 or (row+i) >= n or (col+i) < 0 or (col+i) >=m:
      break
    if grid[row][col] == grid[row+i][col] == grid[row][col+i] == grid[row+i][col+i]:
      ret = i
    i+=1

  return ret+1

for row in range(n):
  for col in range(m):
    ans = max(ans,isSquare(row,col))
print(ans*ans)