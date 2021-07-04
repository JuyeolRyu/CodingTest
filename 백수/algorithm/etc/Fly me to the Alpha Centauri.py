import math
T = int(input())

for t in range(T):
  x,y = map(int,input().split())
  dist = y-x
  if int(math.sqrt(dist)) == math.sqrt(dist):
    print(int(math.sqrt(dist))*2-1)
  else:
    print(math.floor(math.sqrt(dist)*2))

'''
재귀
import sys
sys.setrecursionlimit(100000)
T = int(input())

for t in range(T):
  x,y = map(int,input().split())

  def warp(dist,cur):
    if dist == 0:
      return 1
    ret = float('inf')

    if dist >= (cur+1):
      ret = min(ret,warp(dist-(cur+1),cur+1))
    if dist >= cur and cur > 0:
      ret = min(ret,warp(dist-cur,cur))
    if dist >= (cur-1) and cur-1 > 0:
      ret = min(ret,warp(dist-(cur-1),cur-1))

    return ret+1
  
  print(warp(y-x-1,0))
'''