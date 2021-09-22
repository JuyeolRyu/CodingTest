def solution(n):
    dp = [0]*(n+1)
    dp[2] = 3
    for i in range(4,n+1,2):
        dp[i] += dp[i-2]*3+2
        for j in range(2,i-2,2):
            dp[i] += dp[j]*2
    return dp[-1]%1000000007
