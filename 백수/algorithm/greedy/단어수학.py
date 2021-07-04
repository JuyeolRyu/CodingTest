#https://www.acmicpc.net/problem/1339
import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
alpha = defaultdict(int)
string = []
ans = 0
for _ in range(n):
  string.append(input().rstrip())
#가중치 설정
for s in string:
  len_s = len(s)
  for idx,c in enumerate(s):
    alpha[c] += 10**(len_s-idx-1)
#sort and number change
alpha = dict(sorted(alpha.items(),key = lambda x:x[1],reverse=True))
number = 9
for a in alpha:
  alpha[a] = str(number)
  number -= 1

#alpha to num
for s in string:
  num = ''
  for c in s:
    num += alpha[c]
  ans += int(num)

print(ans)