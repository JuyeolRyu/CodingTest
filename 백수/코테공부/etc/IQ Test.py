#https://www.acmicpc.net/problem/1111
#IQ Test 1111
n = int(input())
arr = list(map(int,input().split()))

if n == 1:
  print("A")
elif n == 2:
  if arr[0] == arr[1]:
    print(arr[0])
  else:
    print("A")
else:
  if arr[1] == arr[0]:
    a = 0
    b = arr[0]
  else:
    a = (arr[2]-arr[1]) // (arr[1]-arr[0])
    b = arr[1] - arr[0]*a
  check = False
  for i in range(1,n):
    if arr[i] != arr[i-1]*a + b:
      check = True
      break

  if check:
    print("B")
  else:
    print(arr[-1]*(a)+b)