#https://www.acmicpc.net/problem/1197
import sys
from collections import deque
input = sys.stdin.readline

def move(r,c,i):
  cnt = 0
  while grid[r+dr[i]][c+dc[i]] != '#':
    r = r+dr[i]
    c = c+dc[i]
    cnt += 1
    if grid[r][c] == 'O':
      break
    
  return r,c,cnt

row,col = map(int,input().split())
grid = [list(input())[:-1] for _ in range(row)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
start = [0,0,0,0,1]
visited = []
ans = -1
#find start
for r in range(row):
  if 'R' in grid[r]:
    start[0] = r
    start[1] = grid[r].index('R')
  if 'B' in grid[r]:
    start[2] = r
    start[3] = grid[r].index('B')

q = deque()
q.append(start)
while q:
  rr,rc,br,bc,c = q.popleft()
  check = False
  #10번 넘기는 경우
  if c > 10:
    ans = -1
    break

  for i in range(4):
    nrr,nrc,rcnt = move(rr,rc,i)
    nbr,nbc,bcnt = move(br,bc,i)

    if grid[nbr][nbc] != 'O':
      #O들어갔을 경우
      if grid[nrr][nrc] == 'O':
        ans = c
        check = True
        break
      #겹친 경우
      if nrr==nbr and nrc==nbc:
        if rcnt > bcnt:
          nrr -= dr[i]
          nrc -= dc[i]
        else:
          nbr -= dr[i]
          nbc -= dc[i]
      if [nrr,nrc,nbr,nbc] not in visited:
        visited.append([nrr,nrc,nbr,nbc])
        q.append([nrr,nrc,nbr,nbc,c+1])
  
  if check:
    break

print(ans)