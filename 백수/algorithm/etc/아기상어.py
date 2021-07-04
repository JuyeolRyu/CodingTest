#https://www.acmicpc.net/problem/16236
import sys,copy
from collections import deque
#입력부
N = int(sys.stdin.readline())
grid = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
dr = [-1,0,0,1]
dc = [0,-1,1,0]
#시작점 찾기
start = [0,0]
for idx,row in enumerate(grid):
  if 9 in row:
    start[0] = idx
    start[1] = row.index(9)
grid[start[0]][start[1]] = 0

#경과시간, 현제 무게, 잡아먹은 수
t = 0
w = 2
stack = 0

while True:
  visited = [[False]*N for _ in range(N)]
  q = deque()
  q.append(start)
  visited[start[0]][start[1]] = True
  dist = 0
  while q:
    #거리 측정, 우선순위 결졍 위해 사용
    tmp_q = []
    while q:
      r,c = q.popleft()
      #갈수 있는 곳인 경우 and 먹이가 있는 경우
      if 0 < grid[r][c] < w:
        #스택+1 and 시간 측정
        stack += 1
        t += dist
        #값 초기화
        dist = 0
        q = deque()
        tmp_q = []
        start[0] =r
        start[1] =c
        visited = [[False]*N for _ in range(N)]
        grid[r][c] = 0

        #스택 다쌓았을 경우 무게 늘리고 스택 초기화
        if stack == w:
          w += 1
          stack = 0
      
      #다음으로 방문할곳 탐색
      for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<N and 0<=nc<N:
          if grid[nr][nc] <= w and not visited[nr][nc]:
            tmp_q.append([nr,nc])
            visited[nr][nc] = True

    #다음 방문지들을 왼쪽위부터 탐색할수 있도록 정렬
    tmp_q = sorted(tmp_q,key = lambda x:(x[0],x[1]))
    for x in tmp_q:
      q.append(x)
    #큐 최신화 and 거리+1
    q = deque(tmp_q)
    dist += 1

  break
print(t)
