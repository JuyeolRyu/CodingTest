####################################
dp = [0]*100
def fibo_top_down(x):
  if x==1 or x==2:
    return 1
  #이미 계산한 적이 있는 경우
  if dp[x] != 0:
    return dp[x]
  
  dp[x] = fibo_top_down(x-1) + fibo_top_down(x-2)
  return dp[x]

print(fibo_top_down(99))
####################################
dp = [0] * 100
dp[1] = 1
dp[2] = 1

for i in range(3,100):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[99])
####################################