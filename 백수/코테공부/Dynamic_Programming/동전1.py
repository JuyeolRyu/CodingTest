#https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline
#value
coin = []
#input
n,k = map(int,input().split())
for _ in range(n):
  coin.append(int(input()))
dp = [0]*(k+1)
dp[0] = 1

for c in coin:
  for num in range(1,k+1):
    if num-c >= 0:
      dp[num] += dp[num-c]

print(dp[-1])


'''
import sys
from collections import defaultdict
input = sys.stdin.readline
#value
coin = []
dp = defaultdict(set)
#input
n,k = map(int,input().split())
for _ in range(n):
  coin.append(int(input()))

for num in range(1,k+1):
  for c in coin:
    if num-c >= 0:
      if not dp[num-c]:
        dp[num].add(str(c))
      else:
        for d in dp[num-c]:
          dp[num].add("".join(sorted(d+str(c))))

print(len(dp[k]))
'''