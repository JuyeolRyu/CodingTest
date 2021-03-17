#https://www.acmicpc.net/problem/2206
import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs():
  q = deque()
  q.append([0,0,1])
  visited = [[[0]*2 for i in range(m)] for j in range(n)]
  visited[0][0][1] = 1
  while q:
    r,c,flag = q.popleft()
    if r == n-1 and c == m-1:
      return visited[r][c][flag]
    
    for i in range(4):
      nr = r+dr[i]
      nc = c+dc[i]

      if 0<=nr<n and 0<=nc<m:
        if road[nr][nc] == 1 and flag == 1:
          visited[nr][nc][0] = visited[r][c][1]+1
          q.append([nr,nc,0])
        elif road[nr][nc] == 0 and visited[nr][nc][flag] == 0:
          visited[nr][nc][flag] = visited[r][c][flag]+1
          q.append([nr,nc,flag])
  return -1
        
n,m = map(int,sys.stdin.readline().split())
road = []
for i in range(n):
  road.append(list(map(int,sys.stdin.readline().strip())))
print(bfs())