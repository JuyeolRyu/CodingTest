#동전
#https://www.acmicpc.net/problem/9084

#sol1(Dynamic Programming)
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int,input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1,m+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    
    print(dp[m])