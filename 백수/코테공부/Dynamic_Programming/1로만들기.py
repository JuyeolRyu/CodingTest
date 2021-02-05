#############################################################
#x가 5로 나누어 떨어지면 5로 나눈다.                          #
#x가 3로 나누어 떨어지면 3로 나눈다.                          #
#x가 2로 나누어 떨어지면 2로 나눈다.                          #
#x에서 1을 뺀다.                                             #
#x를 1로 만든다.                                             #
#############################################################

#1로 만들기
#https://www.acmicpc.net/problem/1463

x = int(input())
ans = 0
dp = [0] * (x+1)

for i in range(2,x+1):
  dp[i] = dp[i-1]+1

  if i % 5 == 0:
    dp[i] = min(dp[i],dp[i//5]+1)
  if i % 3 == 0:
    dp[i] = min(dp[i],dp[i//3]+1)
  if i % 2 == 0:
    dp[i] = min(dp[i],dp[i//2]+1)

print(dp[x])


###################################################################
x = int(input())
dp = [float('inf') for _ in range(x+1)]
dp[-1] = 0

for i in range(x,0,-1):
  if i%3 == 0:
    dp[i//3] = min(dp[i//3],1+dp[i])
  if i%2 == 0:
    dp[i//2] = min(dp[i//2],1+dp[i])
  dp[i-1] = min(dp[i-1],1+dp[i])

print(dp[1])