#https://www.acmicpc.net/problem/1946
#1946 신입사원

T = int(input())
ans = []
for t in range(T):
  N = int(input())
  rank = []
  ans_list = []

  for n in range(N):
    rank.append(list(map(int,input().split())))

  rank = sorted(rank,key=lambda x: x[0])
  min_num = float('inf')

  for i,r in enumerate(rank):
    if r[1] < min_num:
      min_num = r[1]
      ans_list.append(i)

  
  ans.append(len(ans_list))

for i in ans:
  print(i)