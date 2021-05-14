#https://www.acmicpc.net/problem/11404
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijk(start):
  dist = [float('inf')]*(N+1)
  dist[start] = 0
  q = []
  heapq.heappush(q,[0,start])
  while q:
    distance,cur = heapq.heappop(q)
    if dist[cur] < distance:
      continue
    for ne in path[cur]:
      cost = distance+ne[1]
      if cost < dist[ne[0]]:
        dist[ne[0]] = cost
        heapq.heappush(q,[cost,ne[0]])
  for i in range(1,N+1):
    if dist[i] == float('inf'):
      dist[i] = 0
  return dist[1:]

#input
N = int(input())
M = int(input())
path = defaultdict(list)
for i in range(M):
  u,v,c = map(int,input().split())
  path[u].append([v,c])
for s in range(1,N+1):
  for a in dijk(s):
    print(a,end=" ")
  print("")