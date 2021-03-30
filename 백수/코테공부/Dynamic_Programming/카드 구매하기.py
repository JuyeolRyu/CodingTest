#https://www.acmicpc.net/problem/11052
import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(n)]
dp[0] = numbers[0]
for i in range(1,n):
  for j in range(i):
    dp[i] = max(dp[i-j-1]+numbers[j], dp[i],numbers[i])

print(dp[-1])