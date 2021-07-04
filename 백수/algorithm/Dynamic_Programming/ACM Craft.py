#https://www.acmicpc.net/problem/1005
#1005 ACM Craft

#sol1 dp & 위상정렬(topological sort)
import sys
from collections import deque

for t in range(int(input())):
  n,k = map(int,sys.stdin.readline().split())
  need_time = list(map(int,sys.stdin.readline().split()))
  graph = dict()
  indegree = dict()

  for i in range(1,n+1):
    graph[i] = []
    indegree[i] = 0
  #input value
  for i in range(k):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[1])
    indegree[tmp[1]] += 1
  #input target
  target = int(input())
  
  def topSort():
    queue = deque()
    dp = dict()

    for i in graph:
      dp[i] = 0
    for i in graph:
      if indegree[i] == 0:
        queue.append(i)
        dp[i] = need_time[i-1]
    for i in graph:
      cur = queue.popleft()
      if cur == target:
        return dp[cur]
      for j in graph[cur]:
        indegree[j]-=1
        dp[j] = max(dp[j],dp[cur]+need_time[j-1])
        if indegree[j] == 0:
          queue.append(j)

  print(topSort())

#sol2 dp & dfs ==> 시간 초과
from collections import deque
T = int(input())
ans = [float('inf')]*T

for t in range(T):
  n,k = map(int,input().split())
  need_time = list(map(int,input().split()))
  rule1 = dict()
  rule2 = dict()
  start = set()
  dp = [0]*(n+1)
  #input value
  for i in range(k):
    tmp = list(map(int,input().split()))
    start.add(tmp[0])
    start.add(tmp[1])

    if tmp[1] not in rule1:
      rule1[tmp[1]] = [tmp[0]]
    else:
      rule1[tmp[1]].append(tmp[0])
    if tmp[0] not in rule2:
      rule2[tmp[0]] = [tmp[1]]
    else:
      rule2[tmp[0]].append(tmp[1])
  target = int(input())
  start = list(start)
  #find start
  for r in rule1:
    if r in start:
      start.pop(start.index(r))

  
  def dfs(prev,cur):
    dp[cur] = max(dp[cur],dp[prev]+need_time[cur-1])
    
    if cur == target:
      return;

    if cur in rule2: 
      for r in rule2[cur]:
        if r != target and r not in rule2:
          continue
        dfs(cur,r)

    return;

  if target not in rule1:
    ans[t] = need_time[target-1]
  else:
    for s in start: 
      dfs(0,s)
      ans[t] = min(ans[t],dp[target])

for t in range(T):
  print(ans[t])