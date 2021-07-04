#https://www.acmicpc.net/problem/1080
import sys
input = sys.stdin.readline
def flip(r,c):
  for i in range(r,r+3):
    for j in range(c,c+3):
      a[i][j] ^= 1
n,m = map(int,input().split())
a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
b = [list(map(int,list(input().rstrip()))) for _ in range(n)]
ans = 0
for r in range(n-2):
  for c in range(m-2):
    if a[r][c] != b[r][c]:
      flip(r,c)
      ans += 1

if a==b:
  print(ans)
else:
  print(-1)