#https://www.acmicpc.net/problem/14226
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

grid = [[0]*(n+1) for _ in range(n+1)]
q = deque()
q.append([1,0])
while q:
  imo,clip = q.popleft()
  #이모티콘 복사
  if 0< imo < n+1 and grid[imo][imo] == 0:
    q.append([imo,imo])
    grid[imo][imo] = grid[imo][clip]+1
  #이모티콘 붙여넣기
  if clip > 0 and imo+clip < n+1 and grid[imo+clip][clip] == 0:
    q.append([imo+clip,clip])
    grid[imo+clip][clip] = grid[imo][clip]+1
  #이모티콘 한개 삭제
  if imo > 1 and grid[imo-1][clip] == 0:
    q.append([imo-1,clip])
    grid[imo-1][clip] = grid[imo][clip]+1

print(min(grid[-1][1:]))