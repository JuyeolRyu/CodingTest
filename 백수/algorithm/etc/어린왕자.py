import math
T = int(input())

for t in range(T):
  sx,sy,ex,ey = map(int,input().split())
  n = int(input())
  circle = []
  ans = 0
  for c in range(n):
    circle.append(list(map(int,input().split())))
  
  def check(circle):
    stoc = math.sqrt(math.pow(circle[0]-sx,2) + math.pow(circle[1]-sy,2))
    etoc = math.sqrt(math.pow(circle[0]-ex,2) + math.pow(circle[1]-ey,2))
    if (circle[2] >= stoc and circle[2] >= etoc) or (circle[2] <= stoc and circle[2] <= etoc):
      return 0
    return 1

  for c in circle:
    ans += check(c)
  print(ans)