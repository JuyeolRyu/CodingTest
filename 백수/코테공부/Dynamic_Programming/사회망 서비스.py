#https://www.acmicpc.net/problem/2533
#메모리 초과 해결 안됨

#DFS & DP
import sys
from collections import defaultdict
sys.setrecursionlimit(500000)
input = sys.stdin.readline

sns = defaultdict(list)
n = int(input())
visited = []
dp = [[1,0] for i in range(n+1)]

for i in range(n-1):
  u,v = map(int,input().split())
  sns[u].append(v)
  sns[v].append(u)

def dfs(cur):
  visited.append(cur)
  for ne in sns[cur]:
    if ne not in visited:
      dfs(ne)
      dp[cur][0] += dp[ne][1]
      dp[cur][1] += dp[ne][0]

dfs(1)
print(min(dp[1]))

#DFS 메모리 초과
'''
import sys
from collections import defaultdict
sys.setrecursionlimit(500000)
input = sys.stdin.readline

sns = defaultdict(list)
n = int(input())
dp = [1,0]

for i in range(n-1):
  u,v = map(int,input().split())
  sns[u].append(v)
  sns[v].append(u)

def dfs(cur):
  tmp = dp[0]
  dp[0] = dp[1]
  dp[1] = tmp
  dp[0] += len(sns[cur])
  for ne in sns[cur]:
    sns[ne].remove(cur)
    dfs(ne)
  
  return;

dfs(1)
print(min(dp))
'''

#BFS 시간초과
'''
import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

sns = defaultdict(list)
n = int(input())
ans = float('inf')
for i in range(n-1):
  u,v = map(int,input().split())
  sns[u].append(v)
  sns[v].append(u)

q = deque()
q.append(1)
visited = []
depth = 0
cnt1,cnt2 = 1,0
while q:
  tq = deque()
  depth += 1

  while q:
    cur = q.popleft()
    visited.append(cur)
    for ne in sns[cur]:
      if ne not in visited:
        tq.append(ne)
        if depth%2 == 1:
          cnt2 += 1
        else:
          cnt1 += 1
  q = tq

ans = min(cnt1,cnt2)
print(ans)



7
1 4
1 6
2 3
2 6
3 7
4 5
'''