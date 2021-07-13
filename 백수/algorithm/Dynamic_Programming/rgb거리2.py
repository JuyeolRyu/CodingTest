#rgb거리2
#https://www.acmicpc.net/problem/17404

#sol1(Dynamic programming)
import sys
input = sys.stdin.readline
n = int(input())
paint_cost = [list(map(int,input().split())) for _ in range(n)]
ans = float('inf')
for first_color in range(3):
    dp = [[0]*n for _ in range(3)]
    for i in range(3):
        if i == first_color:
            dp[i][0] = paint_cost[0][i]
            continue
        dp[i][0] = float('inf')
    for i in range(1,n):
        dp[0][i] = min(dp[1][i-1],dp[2][i-1])+paint_cost[i][0]
        dp[1][i] = min(dp[0][i-1],dp[2][i-1])+paint_cost[i][1]
        dp[2][i] = min(dp[0][i-1],dp[1][i-1])+paint_cost[i][2]
    
    for i in range(3):
        if i == first_color:
            continue
        ans = min(ans,dp[i][-1])

print(ans)