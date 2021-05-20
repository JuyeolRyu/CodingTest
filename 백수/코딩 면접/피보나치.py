#sol1
n = 15
fibo = [0]*(n+1)
fibo[1] = 1
for i in range(2,n+1):
  fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo[-1])
#sol2
def fibo(n):
  if N == n:
    return li[-1]+li[-2]
  li.append(li[-1]+li[-2])
  return fibo(n+1)
N = 15
li = [0,1]
if N == 0 or N == 1:
  print(li[N])
else:
  print(fibo(2))
#sol3
def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)
print(fibo(15))