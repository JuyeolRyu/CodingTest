#https://www.acmicpc.net/problem/12865
n,k = map(int,input().split())
stuff = []
dp = [0 for i in range(k+1)]
for i in range(n):
  stuff.append(list(map(int,input().split())))

for i in range(n):
  for j in range(k,1,-1):
    if j >= stuff[i][0]:
      dp[j] = max(stuff[i][1]+dp[j-stuff[i][0]],dp[j])

print(dp[k])