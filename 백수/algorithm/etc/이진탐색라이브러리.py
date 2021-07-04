from bisect import bisect_left,bisect_right

n,m = map(int,input().split())
lst = list(map(int,input().split()))

ans = bisect_right(lst,m) - bisect_left(lst,m)

if ans == 0:
  print(-1)
else:
  print(ans)