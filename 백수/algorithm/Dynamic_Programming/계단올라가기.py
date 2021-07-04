#계단올라가기
#https://www.acmicpc.net/status?user_id=back2225&problem_id=2579&from_mine=1
#https://daimhada.tistory.com/181
n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

if n == 1:
  print(stairs[0])
elif n==2:
  print(stairs[0]+stairs[1])
else:
  dp[0] = stairs[0]
  dp[1] = max(dp[0]+stairs[1],stairs[1])
  dp[2] = max(dp[0]+stairs[2], stairs[1]+stairs[2])

  for i in range(3,n):
    dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])
  print(dp[-1])