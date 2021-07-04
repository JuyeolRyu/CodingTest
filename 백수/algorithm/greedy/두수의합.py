'''
두수의 합
https://www.acmicpc.net/problem/3273
'''
import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
x = int(input())
li.sort()
l,r = 0,n-1
ans = 0
while l<r:
  if li[l]+li[r] == x:
    ans += 1
    l+=1
    r-=1
  elif li[l]+li[r] < x:
    l+=1
  elif li[l]+li[r] > x:
    r-=1
print(ans)