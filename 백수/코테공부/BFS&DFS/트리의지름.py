#https://www.acmicpc.net/problem/1167
import sys
from collections import deque
v = int(sys.stdin.readline())
dic = {}

#input
for i in range(1,v+1):
  li = list(map(int,sys.stdin.readline().split()))[:-1]
  for idx in range(1,len(li),2):
    e,cost = li[idx], li[idx+1]

    if li[0] in dic:
      dic[li[0]].append([e,cost])
    else:
      dic[li[0]] = [[e,cost]]

def find_path(start):
  arr = [0 for j in range(v+1)]
  q = deque()
  q.append(start)

  while q:
    s = q.popleft()
    for e,cost in dic[s]:
      if e== start:
        continue
      if arr[e] == 0:
        arr[e] = arr[s]+cost

        q.append(e)

  return arr      

for i in dic:
  li = find_path(i)
  s = li.index(max(li))
  print(max(find_path(s)))
  break