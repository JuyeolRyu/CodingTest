#https://www.acmicpc.net/problem/2212
#센서
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
if n<k:
  print(0)
else:
  sensor = list(set(map(int,sys.stdin.readline().split())))
  sensor.sort()
  diff = []
  for i in range(1,len(sensor)):
    diff.append(sensor[i]-sensor[i-1])

  diff.sort(reverse=True)

  for i in range(k-1):
    diff.pop(0)
  print(sum(diff))