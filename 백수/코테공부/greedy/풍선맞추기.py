#https://www.acmicpc.net/problem/11509
import sys

n = int(sys.stdin.readline())
balloon = list(map(int,sys.stdin.readline().split()))
arrow = []
ans = 0
for b in balloon:
  if b in arrow:
    arrow[arrow.index(b)] -= 1
  else:
    arrow.append(b-1)
    ans += 1
print(ans)
