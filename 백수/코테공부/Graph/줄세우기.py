#https://www.acmicpc.net/problem/2252
from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
dic = defaultdict(list)
tp_li = defaultdict(int)
for m in range(M):
  a,b = map(int,input().split())
  dic[a].append(b)
  tp_li[b] += 1

q = deque()
ans = []

for i in range(1,N+1):
  if tp_li[i] == 0:
    q.append(i)
    ans.append(i)

while q:
  cur = q.popleft()
  for d in dic[cur]:
    tp_li[d] -= 1
    if tp_li[d] == 0:
      q.append(d)
      ans.append(d)

for a in ans:
  print(a,end=' ')