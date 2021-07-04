#https://www.acmicpc.net/problem/1753
import heapq
v,e = map(int,input().split())
start = int(input())
graph = [[] for i in range(v+1)]

for i in range(e):
  s,e,w = map(int,input().split())
  graph[s].append([e,w])

def dijk(v,k,graph):
  d = [float('inf')]*(v+1)
  d[k] = 0
  
  hq = []
  heapq.heappush(hq,[0,k])

  while hq:
    cost,node = heapq.heappop(hq)
    
    if cost > d[node]:
      continue
    for n in graph[node]:
      next_node = n[0]
      next_cost = d[node]+n[1]
      if next_cost < d[next_node]:
        d[next_node] = next_cost
        heapq.heappush(hq,[next_cost,next_node])
  return d                           
ans = dijk(v,start,graph)
for a in ans[1:]:
  if a == float('inf'):
    print('INF')
  else:
    print(a)