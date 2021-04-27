#https://www.acmicpc.net/problem/11049
import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
  li.append(list(map(int,input().split())))
dp = [[0]*n for _ in range(n)]

for i in range(1,n):
  for j in range(n-i):
    dp[j][j+i] = float('inf')
    for k in range(j,j+i):
      dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i]+li[j][0]*li[k][1]*li[j+i][1])

print(dp[0][-1])


'''
#점화식에 문제 있음(일차원 dp)
import sys
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
  li.append(list(map(int,input().split())))

dp = [0]*n
fNum = li[0][0]
dp[1] = fNum*li[1][0]*li[1][1]

for i in range(2,n):
  print(i,dp[i-1]+(fNum*li[i][0]*li[i][1]), dp[i-2]+(li[i-1][0]*li[i][0]*li[i][1])+(fNum*li[i-1][0]*li[i][1]) )
  dp[i] = min( (dp[i-1]+(fNum*li[i][0]*li[i][1])) , (dp[i-2]+(li[i-1][0]*li[i][0]*li[i][1])+(fNum*li[i-1][0]*li[i][1])) )

print(dp[-1])
'''