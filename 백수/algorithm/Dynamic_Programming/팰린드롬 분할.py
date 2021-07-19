#미친 로봇
#https://www.acmicpc.net/problem/1405

#sol1(dp)
import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
dp = [[0]*(n+1) for _ in range(n+1)]
ans = [float('inf')]*(n+1)
ans[0] = 0

for i in range(1,n+1):
    dp[i][i] = 1
for i in range(1,n):
    if s[i-1] == s[i]:
        dp[i][i+1] = 1

for i in range(2,n):
    for j in range(1,n+1-i):
        if s[j-1] == s[j+i-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(1,n+1):
    ans[i] = min(ans[i],ans[i-1]+1)
    for j in range(i+1,n+1):
        if dp[i][j] != 0:
            ans[j] = min(ans[j],ans[i-1]+1)
print(ans[n])