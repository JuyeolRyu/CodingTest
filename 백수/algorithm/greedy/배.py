#https://www.acmicpc.net/problem/1092
num_crane = int(input())
crane = list(map(int,input().split()))
crane = sorted(crane,reverse = True)
num_box = int(input())
box = list(map(int,input().split()))
box = sorted(box,reverse = True)
can_lift = []
for i,c in enumerate(crane):
  cnt = 0
  for b in box:
    if c >= b:
      cnt += 1
  can_lift.append(cnt)
if max(box) > max(crane):
  print(-1)
else:
  ans = 0
  while len(box) > 0:
    ans += 1
    for c in crane:
      for i in range(len(box)):
        if box[i]<=c:
          box.pop(i)
          break
  print(ans)