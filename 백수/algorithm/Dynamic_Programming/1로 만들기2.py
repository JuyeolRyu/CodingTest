#1로 만들기2
#https://www.acmicpc.net/problem/12852

#sol1(dp)
import sys
input = sys.stdin.readline

n = int(input())
dp = [[float('inf'),i] for i in range(n+1)]
dp[n] = [0,-1]
ans = []
for i in range(n,1,-1):
    if i%3 == 0 and dp[i][0]+1<dp[i//3][0]:
        dp[i//3] = [dp[i][0]+1, i]
    if i%2 == 0 and dp[i][0]+1<dp[i//2][0]:
        dp[i//2] = [dp[i][0]+1, i]
    if dp[i][0]+1<dp[i-1][0]:
        dp[i-1] = [dp[i][0]+1, i]
idx = 1

while dp[idx][1] != -1:
    ans.append(idx)
    idx = dp[idx][1]
ans.append(n)
print(dp[1][0])
for a in list(reversed(ans)):
    print(a,end=' ')