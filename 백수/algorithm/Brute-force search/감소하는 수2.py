#https://www.acmicpc.net/problem/15651
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