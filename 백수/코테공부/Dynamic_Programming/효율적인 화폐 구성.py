n,m = list(map(int,input().split()))
arr = []
for i in range(n):
  arr.append(int(input()))
dp = [float('inf')]*(m+1)

for i in range(1,m+1):
  if i in arr:
    dp[i] = 1
    continue
  for num in arr:
    if 0<=i-num<m+1:
      dp[i] = min(dp[i],dp[i-num]+1)
  
if dp[m] == float('inf'):
  print(-1)
else:
  print(dp[m])