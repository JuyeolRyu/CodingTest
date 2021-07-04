#https://www.acmicpc.net/problem/1052

#sol1 이진수
n,k = map(int,input().split())
bin_n = bin(n).count('1')
ans = 0
while bin_n > k:
  r_n = list(reversed(bin(n)))
  i = 2**r_n.index('1')
  n += i
  ans += i
  bin_n = bin(n).count('1')

print(ans)

#sol2 시간초과
from queue import PriorityQueue
n,k = map(int,input().split())

q = PriorityQueue()
for i in range(n):
  q.put(1)

ret = 0
while q.qsize() > k:
  x = q.get()
  y = q.get()
  if x == y:
    q.put(x+y)
  else:
    tmp = abs(x-y)
    ret += tmp
    if x > y:
      q.put(tmp+x)
    else:
      q.put(tmp+y)

print(ret)