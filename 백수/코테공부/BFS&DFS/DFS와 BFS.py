#https://www.acmicpc.net/problem/1260

from collections import deque
import sys
sys.setrecursionlimit(99999)

n,m,v = list(map(int,input().split()))
vertices = []
dic = dict()

for _ in range(m):
  s,e = map(int,input().split())

  if s not in dic:
    dic[s] = [e]
  else:
    dic[s].append(e)
  
  if e not in dic:
    dic[e] = [s]
  else:
    dic[e].append(s)

for key in dic:
  dic[key] = sorted(dic[key])

ans = []
ans2 = []
visited = []

def dfs(start):
  visited.append(start)
  ans.append(start)
  if len(visited) == n or start not in dic:
    return;
 
  for next in dic[start]:
    if next not in visited:
      dfs(next)

def bfs(start):
  q = deque()
  q.append(start)
  visited.append(start)
  while q:
    node = q.popleft()
    ans2.append(node)
    if node not in dic:
      continue
    for next in dic[node]:
      if next not in visited:
        q.append(next)
        visited.append(next)
dfs(v)
visited = []
bfs(v)

print(' '.join(map(str,ans)))
print(' '.join(map(str,ans2)))