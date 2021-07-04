#https://www.acmicpc.net/problem/3665
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
answer = []
for t in range(int(input())):
  n = int(input())
  li = list(map(int,input().split()))
  dic = defaultdict(list)
  degree = defaultdict(int)
  q = deque()
  ans = []
  for i,num in enumerate(li):
    dic[num] = li[i+1:]
    degree[num] += i

  for i in range(int(input())):
    l,r = map(int,input().split())
    if l in dic[r]:
      dic[r].remove(l)
      dic[l].append(r)
      degree[r] += 1
      degree[l] -= 1
    else:
      dic[l].remove(r)
      dic[r].append(l)
      degree[l] += 1
      degree[r] -= 1

  for d in degree:
    if degree[d] == 0:
      q.append(d)
  
  while q:
    cur = q.popleft()
    ans.append(cur)
    for ne in dic[cur]:
      degree[ne] -= 1
      if degree[ne] == 0:
        q.append(ne)

  if len(ans) == len(li):
    answer.append(ans)
  else:
    answer.append('IMPOSSIBLE')

for ans in answer:
  if ans == 'IMPOSSIBLE':
    print('IMPOSSIBLE')
  else:
    for a in ans:
      print(a,end=' ')
    print('')