T = int(input())
for t in range(T): 
  n,m = list(map(int,input().split()))
  arr_input = list(map(int,input().split()))
  arr = []
  dp = [[0 for _ in range(m)] for i in range(n)]
  #dp테이블 초기화
  for i in range(n):
    arr.append(arr_input[i*m:i*m+m])
    dp[i][0] = arr[i][0]
  #dp시작
  for col in range(1,m):
    for row in range(n):
      if 0<= row-1 < n:
        dp[row][col] = max(dp[row-1][col-1]+arr[row][col],dp[row][col])
      if 0<= row < n:
        dp[row][col] = max(dp[row][col-1]+arr[row][col],dp[row][col])
      if 0<= row+1 < n:
        dp[row][col] = max(dp[row+1][col-1]+arr[row][col],dp[row][col])
  
  ans = 0

  for row in range(n):
    ans = max(ans,dp[row][-1])
  print(ans)