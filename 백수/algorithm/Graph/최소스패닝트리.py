#https://www.acmicpc.net/problem/1197
import sys
input = sys.stdin.readline

def find(x):
  if x == parent[x]:
    return x
  x = find(parent[x])
  return x
def union(x,y):
  x = find(x)
  y = find(y)
  parent[x] = y

V,E = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(E)]
graph = sorted(graph,key=lambda x:x[2])
parent = [i for i in range(V+1)]
ans = 0
while graph:
  u,v,c = graph.pop(0)
  if find(u) == find(v):
    continue
  else:
    ans += c
    union(u,v)
print(ans)