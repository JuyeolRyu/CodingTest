#https://www.acmicpc.net/problem/1238
#파티 1238
from heapq import heappush, heappop
n,m,x = map(int,input().split())
road = [[] for _ in range(n+1)]
road2 = [[] for _ in range(n+1)]
dp = [float('inf') for _ in range(n+1)]
dp2 = [float('inf') for _ in range(n+1)]
for _ in range(m):
  s,e,w = map(int,input().split())
  road[s].append([e,w])
  road2[e].append([s,w])

def dijstra(start,dp,road):
  heap = []
  dp[start] = 0
  heappush(heap,[0,start])
  while heap:
    w,n = heappop(heap)
    if dp[n] < w:
      continue
    for nn,weight in road[n]:
      nw = weight+w
      if nw < dp[nn]:
        dp[nn]=nw
        heappush(heap,[nw,nn])

dijstra(x,dp,road)
dijstra(x,dp2,road2)
max_val = 0
for i in range(1,n+1):
  max_val = max(max_val,dp[i]+dp2[i])
print(max_val)