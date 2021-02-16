#https://www.acmicpc.net/workbook/view/2052
#재귀함수 연습
#1
from itertools import permutations
n,m = map(int,input().split())
lst = [i+1 for i in range(n)]

for row in list(permutations(lst,m)):
  for r in row:
    print(r,end=' ')
  print()
#2
from itertools import combinations
n,m = map(int,input().split())
lst = [i+1 for i in range(n)]

for row in list(combinations(lst,m)):
  for r in row:
    print(r,end=' ')
  print()
#3
n,m = map(int,input().split())
ans = []
def sol(digit,lst):
  if digit == m+1:
    ans.append(lst)
    return
  
  for i in range(1,n+1):
    sol(digit+1,lst+[i])
  return;

sol(1,[])
for row in ans:
  for r in row:
    print(r,end=" ")
  print()