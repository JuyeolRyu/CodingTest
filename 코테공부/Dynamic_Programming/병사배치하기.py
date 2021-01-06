n = int(input())
arr = list(map(int,input().split()))
arr.reverse()
dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))