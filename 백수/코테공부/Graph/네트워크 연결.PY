#https://www.acmicpc.net/problem/1922
import sys
from queue import PriorityQueue
import heapq
input = sys.stdin.readline

def find(x):
  if x==parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]
def union(x,y):
  x = find(x)
  y = find(y)
  parent[x] = y

n = int(input())
graph = []
visited = []
for i in range(int(input())):
  u,v,c = map(int,input().split())
  heapq.heappush(graph,[c,u,v])
parent = [i for i in range(0,n+1)]
ans = 0
while graph:
  c,u,v = heapq.heappop(graph)
  #사이클 확인
  if find(u) == find(v):
    continue
  else:
    ans += c
    union(u,v)
print(ans)


'''
import sys
from queue import PriorityQueue
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dic = defaultdict(list)
for i in range(int(input())):
  a,b,c = map(int,input().split())
  dic[a].append([b,c])
  dic[b].append([a,c])

def kruskal(s):
  ans = 0
  q = PriorityQueue()
  visited = [s]
  for v,c in dic[s]:
    q.put((c,v))
  while True:
    if len(visited) == n:
      break
    c,u = q.get()

    if u in visited:
      continue
    else:
      ans += c
      visited.append(u)
      for v,c in dic[u]:
        if v not in visited:
          q.put((c,v))

  return ans

print(kruskal(1))
'''