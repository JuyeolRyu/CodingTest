#https://www.acmicpc.net/problem/1516
#위상정렬
import sys
from collections import deque

n = int(sys.stdin.readline())
building = {}
cost = [0 for i in range(n+1)]
ans = [0 for i in range(n+1)]
degree = [0 for i in range(n+1)]
q = deque()

for i in range(n):
  build = list(map(int,sys.stdin.readline().split()))
  cost[i+1] = build[0]
  for j in build[1:-1]:
    if j in building:
      building[j].append(i+1)
    else:
      building[j] = [i+1]
    degree[i+1] += 1

for i in range(1,n+1):
  if degree[i] == 0:
    q.append(i)
    ans[i] = cost[i]

while q:
  cur = q.popleft()
  if cur in building:
    for ne in building[cur]:
      degree[ne] -= 1
      ans[ne] = max(ans[ne], cost[ne]+ans[cur])

      if degree[ne] == 0:
        q.append(ne)

for a in ans[1:]:
  print(a)

'''
4
1 4 3 2 -1
2 4 -1
1 4 -1
1 -1
'''