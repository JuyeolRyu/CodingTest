#https://www.acmicpc.net/problem/10942
import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
quest = [list(map(int,sys.stdin.readline().split())) for i in range(m)]
dp = [[0 for i in range(n)] for j in range(n)]

for i in range(n-1):
  dp[i][i] = 1
  if numbers[i] == numbers[i+1]:
    dp[i][i+1] = 1
  else:
    dp[i][i+1] = 0
dp[-1][-1] = 1
for c in range(2,n):
  for r in range(0,n-c):
    if numbers[r] == numbers[r+c] and dp[r+1][r+c-1] == 1:
      dp[r][r+c] = 1
    '''
    i = r
    j = i+c
    print(i,j)
    '''
for s,e in quest:
  print(dp[s-1][e-1])