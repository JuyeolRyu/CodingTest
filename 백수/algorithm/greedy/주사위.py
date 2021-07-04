#https://www.acmicpc.net/problem/1041
import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int,input().split()))
my_sum = float('inf')
min_set = []
ans = 0

if n == 1:
  print(sum(dice)-max(dice))
else:
  #합이 제일 작은 조합 고르기
  num_set = [[0,1,2],[0,1,3],[0,2,4],[0,3,4],[5,1,2],[5,1,3],[5,2,4],[5,3,4]]
  for num in num_set:
    if sum([dice[num[0]],dice[num[1]],dice[num[2]]]) < my_sum:
      my_sum = sum([dice[num[0]],dice[num[1]],dice[num[2]]])
      min_set = [dice[num[0]],dice[num[1]],dice[num[2]]]
  #정렬
  min_set.sort()
  #기둥 부분의 합
  ans += (((min_set[0]+min_set[1])*n*4) + min_set[2]*4)
  #벽면의 합
  ans += n*(n-2)*min_set[0]*4
  #천장의 합
  ans += ((n*n-(n-2)*(n-2)-4)*min_set[1] + (n-2)*(n-2)*min_set[0])

  print(ans)

'''
3
1 1 1 1 1 1
'''