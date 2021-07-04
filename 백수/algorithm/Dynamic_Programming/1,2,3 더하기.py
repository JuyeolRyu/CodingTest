T = int(input())
for t in range(T):
  n = int(input())
  dp = [0 for i in range(n+1)]
  for i in range(1,n+1):
    if i == 1 or i == 2 or i == 3:
      dp[i] = 1

    if i-1 >= 0:
      dp[i] += dp[i-1]
    if i-2 >= 0:
      dp[i] += dp[i-2]
    if i-3 >= 0:
      dp[i] += dp[i-3]

  print(dp[-1])