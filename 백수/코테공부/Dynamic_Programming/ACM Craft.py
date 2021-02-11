from collections import deque
T = int(input())

for t in range(T):
  n,k = map(int,input().split())
  need_time = list(map(int,input().split()))
  rule1 = dict()
  rule2 = dict()
  start = set()
  ans = [0]*(n+1)
  #input value
  for i in range(k):
    tmp = list(map(int,input().split()))
    start.add(tmp[0])
    start.add(tmp[1])

    if tmp[1] not in rule1:
      rule1[tmp[1]] = [tmp[0]]
    else:
      rule1[tmp[1]].append(tmp[0])
    if tmp[0] not in rule2:
      rule2[tmp[0]] = [tmp[1]]
    else:
      rule2[tmp[0]].append(tmp[1])
  target = int(input())
  start = list(start)
  #find start
  for r in rule1:
    if r in start:
      start.pop(start.index(r))

  for s in start:
    q = deque()
    q.append(s)
    idx=1
    #dp
    while q:
      tmp_q = deque()
      while q:
        cur = q.popleft()
        ans[idx] = max(ans[idx],ans[idx-1]+need_time[cur-1])

        if cur ==target:
          print(ans[idx])
          break

        if cur in rule2: 
          for r in rule2[cur]:
            if cur in rule1[r]:
              rule1[r].pop(rule1[r].index(cur))
            if rule1[r] == []:
              tmp_q.append(r)
      q = tmp_q
      idx+=1