#https://www.acmicpc.net/problem/1541
import sys
import re
input = sys.stdin.readline

s = input().rstrip()
li = []
num = ''
for c in s:
  if c.isdigit():
    num += c
  elif c == '+' or c =='-':
    li.append(num)
    li.append(c)
    num = ''
li.append(num)
if li[0] == '':
  li = li[1:]
ans = 0
idx = 0
while idx < len(li):
  if li[idx].isdigit():
    ans += int(li[idx])
    idx+=1
  elif li[idx] == '+':
    idx += 1
    continue
  elif li[idx] == '-':
    tmp = 0
    idx += 1
    while idx < len(li):
      if li[idx].isdigit():
        tmp += int(li[idx])
        idx+=1
      elif li[idx] == '+':
        idx += 1
        continue
      elif li[idx] == '-':
        break
    ans-=tmp
print(ans)


'''
-1+1+1+1-1-1
'''