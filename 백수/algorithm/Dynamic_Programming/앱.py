#앱
#https://www.acmicpc.net/problem/7579

#sol1(dp)
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = [0]+list(map(int,input().split()))
C = [0]+list(map(int,input().split()))
ans = sum(C)

dp = [[0]*(sum(C)+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(sum(C)+1):
        if C[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-C[i]]+A[i],dp[i-1][j])
        
        if dp[i][j] >= M:
            ans = min(ans,j)

if ans == 0:
    print(0)
else:
    print(ans)