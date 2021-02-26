#https://www.acmicpc.net/problem/1256

#sol1 dp&문자열
from math import factorial
n,m,k = map(int,input().split())
ans = ''
a = n
z = m
dp = []

if int(factorial(a+z)/(factorial(a)*factorial(z))) < k:
  print(-1)
else:
  while True:
    tmp = int( factorial(a+z)/(factorial(a)*factorial(z)) )
    if tmp > k:
      dp.append('a')
      a-=1
    elif tmp == k:
      dp.append('z'*z+'a'*a)
      break
    else:
      k-= int(factorial(a+z)/(factorial(a)*factorial(z)))
      dp.pop(-1)
      dp.append('z')
      a+=1
      z-=1

  for c in dp:
    print(c,end='')
  print()

'''
#sol2 그냥풀기==>시간초과 
from itertools import permutations

n,m,k = map(int,input().split())
s = 'a'*n+'z'*m
s_set = sorted(set(permutations(s,n+m)))
if len(s_set) < k:
  print(-1)
else:
  for c in s_set[k-1]:
    print(c,end='')
  print()
'''

