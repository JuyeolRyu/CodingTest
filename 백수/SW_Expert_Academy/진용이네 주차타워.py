from collections import deque

T = int(input())

for _ in range(T):
  n,m = map(int,(input().split()))
  price = []
  weight = []

  queue = [-1 for i in range(n)]
  waiting_queue = deque()

  ans = 0

  for i in range(n):
    price.append(int(input()))
  for i in range(m):
    weight.append(int(input()))

  for i in range(2*m):
    cur = int(input())
    if(cur < 0):
      cur = abs(cur)
      queue[queue.index(cur)] = -1
      if(len(waiting_queue) > 0):
        idx = queue.index(-1)
        cur = waiting_queue.popleft()
        queue[idx]= cur
        ans += price[idx]*weight[cur-1]
    else:
      try:
        idx = queue.index(-1)
        queue[idx] = cur
        ans += price[idx]*weight[cur-1]
      except:
        waiting_queue.append(cur)
      
  print(ans)
