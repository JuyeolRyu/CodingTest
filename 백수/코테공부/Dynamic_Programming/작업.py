#https://www.acmicpc.net/problem/2056
import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline
n = int(input())

dic = defaultdict(list)
degree = defaultdict(int)
cost = [0]*(n+1)
dp = [0]*(n+1)
for i in range(1,n+1):
  tmp = list(map(int,input().split()))
  cost[i] = tmp[0]

  if tmp[1] != 0:
    for num in tmp[2:]:
      dic[num].append(i)
    degree[i] += tmp[1]
  
q = deque()
for i in range(1,n+1):
  if degree[i] == 0:
    q.append(i)
    dp[i] = cost[i]
while q:
  cur = q.popleft()
  for ne in dic[cur]:
    degree[ne] -= 1
    dp[ne] = max(dp[ne],dp[cur]+cost[ne])
    if degree[ne] == 0:
      q.append(ne)

print(max(dp))

'''
7
5 0
1 1 1
3 1 2
6 1 1
8 2 2 4
1 2 2 4
4 3 3 5 6

4
10 0
6 1 1
7 1 1
5 1 2

7
5 0
1 0
3 0
6 0
1 0
8 0
4 0

3
100 0
10 0
5 2 1 2
'''