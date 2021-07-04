#https://www.acmicpc.net/problem/1038
#1038 감소하는 수
n = int(input())
ans = []
def sol(num,digit):
  global ans
  if digit > 10 or len(ans) >=1023:
    return
  ans.append(num)

  for i in range(10):
    if num%10 > i:
      sol((num*10)+i,digit+1)
  return;
  

if n > 1022:
  print(-1)
else:
  for num in range(10):
    sol(num,1)
  ans = sorted(ans)
  print(ans[n])