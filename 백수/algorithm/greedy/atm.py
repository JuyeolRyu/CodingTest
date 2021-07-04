#https://www.acmicpc.net/problem/11399
import sys
input = sys.stdin.readline

ans = 0
n = int(input())
p = list(map(int,input().split()))
p.sort()

for i in range(n):
    ans += sum(p[:i+1])

print(ans)