#https://www.acmicpc.net/problem/1062
#1062 가르침
from itertools import combinations
n,m = map(int,input().split())
lst = []
word_set = ['a','c','i','n','t']
word_lst = []

for i in range(n):
  s = input()[4:-4]
  tmp = ''
  for c in s:
    if c not in word_set:
      tmp += c
  s = list(set(list(tmp)))
  lst.append(s)

if m < 5:
  print(0)
else:
  for i in range(n):
    word_lst.extend(lst[i])
  word_lst = list(set(word_lst))

  ans = 0
  if len(word_lst) < m-5:
    m = len(word_lst)
  else:
    m -= 5
  for i in map(list,(combinations(word_lst,m))):
    cnt = 0
    for s in lst:
      check = True
      for c in s:
        if c not in i:
          check = False
          break
      if check:
        cnt += 1
    ans = max(ans,cnt)
  print(ans)