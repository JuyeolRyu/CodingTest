#https://www.acmicpc.net/problem/14503
import sys
n,m = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
grid = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
ans = 0
while True:
  if grid[r][c] == 0:
    grid[r][c] = 2
    ans += 1
  check = False
  tmpd = d
  for i in range(4):
    if d == 0:
      if grid[r][c-1] == 0:
        c = c-1
        d = 3
        check = True
        break
      else:
        d = 3
    elif d == 1:
      if grid[r-1][c] == 0:
        r = r-1
        d = 0
        check = True
        break
      else:
        d = 0
    elif d == 2:
      if grid[r][c+1] == 0:
        c = c+1
        d = 1
        check = True
        break
      else:
        d = 1
    elif d == 3:
      if grid[r+1][c] == 0:
        r = r+1
        d = 2
        check = True
        break
      else:
        d = 2
    
  if not check:
    d = tmpd
    if d == 0:
      r = r+1  
    elif d == 1:
      c = c-1
    elif d == 2:
      r = r-1
    elif d == 3:
      c = c+1

    if grid[r][c] == 1:
      break

print(ans)
#0 0 -1
#1 -1 0
#2 0 1
#3 1 0