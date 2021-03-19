#https://www.acmicpc.net/problem/11497
import sys
for t in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  numbers = list(map(int,sys.stdin.readline().split()))
  numbers.sort()
  ans = numbers[1]-numbers[0]
  for i in range(2,n):
    ans = max(ans,numbers[i]-numbers[i-2],numbers[i]-numbers[i-1])
  
  print(ans)