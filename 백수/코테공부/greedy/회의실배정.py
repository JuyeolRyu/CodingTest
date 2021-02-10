#https://www.acmicpc.net/problem/1931
#1931 회의실 배정

n = int(input())
T = []
for i in range(n):
  T.append(list(map(int,input().split())))
T = sorted(T,key= lambda x: (x[1],x[0]))

ans = 0
end = 0
for t in T:
  if t[0] >= end:
    ans += 1
    end = t[1]

print(ans)