def solution(n):
    dp = [True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if dp[i]:
            for j in range(i+i,n+1,i):
                dp[j] = False
    return dp[2:].count(True)