#https://www.acmicpc.net/problem/2156
n = int(input())
li = [int(input()) for i in range(n)]
dp = [0 for i in range(n+1)]

if n <= 2:
  print(sum(li))
else:
  dp[1] = li[0]
  dp[2] = li[1]+dp[1]
  for i in range(3,n+1):
    dp[i] = max(li[i-1]+li[i-2]+dp[i-3], li[i-1]+dp[i-2],dp[i-1])

  print(dp[-1])
'''
7
100
100
1
1
1
100
100
'''