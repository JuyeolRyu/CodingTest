import queue
from sys import stdin

n, k = stdin.readline().split()
n = int(n)
k = int(k)
li = []
for i in range(n):
  x,y=stdin.readline().split()
  x = int(x)
  y = int(y)
  li.append([x,y])

for i in range(k):
  li.append([int(stdin.readline()),2000000])

li.sort()
ans = 0
pq = queue.PriorityQueue(n)
for x in li:
  if x[1] != 2000000:
    pq.put(-x[1])
  else:
    if not pq.empty():
      tmp = -pq.get()
      ans += tmp
    
print(ans)


'''
1 1
100 1
5

4 3
2 99
1 99
3 99
2 5
2
5
3

n, k = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]
bag = [int(input()) for i in range(k)]
ans = 0
li = sorted(li, key = lambda x: (x[0],x[1]))
bag = sorted(bag, key = lambda x:x)

for weight in bag:
  idx = 0
  tmp_i = -1
  tmp_v = -1
  while idx < len(li) and li[idx][0] <= weight:
    if li[idx][1] > tmp_v:
      tmp_v = li[idx][1]
      tmp_i = idx
    idx+= 1
  
  if tmp_v > -1:
    ans += tmp_v
    li.pop(tmp_i)
print(ans)


import sys
n, k = map(int,sys.stdin.readline().split())
dic = dict()
ans = 0

for i in range(n):
  w,v = map(int,sys.stdin.readline().split())
  if w not in dic:
    dic[w] = [v]
  else:
    dic[w].append(v)
dic = dict(sorted(dic.items()))
for i in dic:
  dic[i] = sorted(dic[i])

bag = [int(input()) for i in range(k)]
bag = sorted(bag, key = lambda x:x)
for weight in bag:
  tmp_i = -1
  tmp_v = -1
  for w in dic:
    if w <= weight and len(dic[w]) > 0:
      if tmp_v < dic[w][-1]:
        tmp_i = w
        tmp_v = dic[w][-1]
  if tmp_i > -1:
    ans += tmp_v
    dic[tmp_i].pop(-1)

print(ans)

'''