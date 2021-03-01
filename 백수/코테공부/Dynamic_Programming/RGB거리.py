n = int(input())
house = []
for i in range(n):
  house.append(list(map(int,input().split())))

dp = [[0 for i in range(4)] for j in range(n+1)]
dp[1][1] = house[0][0]
dp[1][2] = house[0][1]
dp[1][3] = house[0][2]

for i in range(1,n+1):
  dp[i][1] = min(dp[i-1][2],dp[i-1][3]) + house[i-1][0]
  dp[i][2] = min(dp[i-1][1],dp[i-1][3]) + house[i-1][1]
  dp[i][3] = min(dp[i-1][2],dp[i-1][1]) + house[i-1][2]

print(min(dp[n][1],dp[n][2],dp[n][3]))