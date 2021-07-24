#무한 수열
#https://www.acmicpc.net/problem/1351

#sol1(Dynamic Programming)
import sys
def dfs(num):
    if dp.get(num):
        return dp[num]

    dp[num] = dfs(num//p) + dfs(num//q)
    return dp[num]

input = sys.stdin.readline
n,p,q = map(int,input().split())
dp = {}
dp[0],dp[1] = 1,2
dfs(n)
print(dp[n])