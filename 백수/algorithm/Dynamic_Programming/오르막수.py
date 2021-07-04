#https://www.acmicpc.net/problem/11057
#오르막수
import sys

n = int(sys.stdin.readline())
dp = [[0 for i in range(10)] for j in range(n)]
dp[0] = [1,1,1,1,1,1,1,1,1,1]

if n == 1:
  print(sum(dp[-1]))
else:
  for i in range(1,n):
    for j in range(10):
      dp[i][j] = sum(dp[i-1][j:])

  print(sum(dp[-1])%10007)