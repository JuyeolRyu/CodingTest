#https://www.acmicpc.net/problem/1019

import sys
input = sys.stdin.readline

n = int(input())
ans = [0]*10
tmp = 1 #자리수

while n > 0:
  while n%10 != 9:
    for i in str(n):
      ans[int(i)] += tmp
    n-=1
  print(n)
  if n < 10:
    for i in range(n+1):
      ans[i] += tmp
    ans[0] -= tmp
    break
  else:
    for i in range(10):
      ans[i] += (n//10+1)*tmp
  ans[0] -= tmp
  tmp *= 10
  n //= 10

for a in ans[:-1]:
  print(a,end=' ')
print(ans[-1])

'''
126
완전탐색
for s in range(1,n+1):
  for c in str(s):
    ans[int(c)] += 1

for a in ans[:-1]:
  print(a,end=' ')
print(ans[-1])
'''