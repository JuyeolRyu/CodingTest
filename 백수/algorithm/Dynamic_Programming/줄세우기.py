#https://www.acmicpc.net/problem/2631
import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
  li.append(int(sys.stdin.readline()))
lis = [-float('inf'),li[0]]

#find LIS
for i in range(1,n):
  if li[i] > lis[-1]:
    lis.append(li[i])
  else:
    for j in range(1,len(lis)):
      if li[i] <= lis[j]:
        lis[j] = li[i]
        break

print(n-len(lis)+1)


'''
6
1
4
2
5
3
6
'''