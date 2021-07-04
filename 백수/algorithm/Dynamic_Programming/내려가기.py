#https://www.acmicpc.net/problem/2096
n = int(input())
grid = [[int(x) for x in input().split()]for i in range(n)]

dp = [[0]*3 for i in range(n)]
dp2 = [[0]*3 for i in range(n)]
if n == 1:
  print(max(grid[0]),min(grid[0]))
else:
  for r in range(n):
    dp[r][0] += max(dp[r-1][0],dp[r-1][1]) + grid[r][0]
    dp[r][1] += max(dp[r-1][0],dp[r-1][1],dp[r-1][2]) + grid[r][1]
    dp[r][2] += max(dp[r-1][1],dp[r-1][2]) + grid[r][2]
    dp2[r][0] += min(dp2[r-1][0],dp2[r-1][1]) + grid[r][0]
    dp2[r][1] += min(dp2[r-1][0],dp2[r-1][1],dp2[r-1][2]) + grid[r][1]
    dp2[r][2] += min(dp2[r-1][1],dp2[r-1][2]) + grid[r][2]

  print(max(dp[-1]),min(dp2[-1]))