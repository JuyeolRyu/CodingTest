#https://www.acmicpc.net/problem/1759
import sys

l,c = map(int,sys.stdin.readline().split())
s = sys.stdin.readline().split()
ans = set()
vowel = ['a','e','i','o','u']
s.sort()

def find(depth,idx,string):
  if depth == l+1:
    cnt = 0
    for i in range(5):
      if vowel[i] in string:
        cnt += 1
    if 1<=cnt<l-1:
      ans.add(string)
    return

  for i in range(idx,c-l+depth):
    find(depth+1,i+1,string+s[i])

find(1,0,'')
ans = list(sorted(ans))
for str in ans:
  print(str)