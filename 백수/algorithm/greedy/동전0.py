#https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

ans = 0
n,k = map(int,input().split())
coins = [ int(input()) for _ in range(n)]
coins.sort(reverse=True)

for coin in coins:
    if coin<=k:
        ans += k//coin
        k = k%coin

print(ans)