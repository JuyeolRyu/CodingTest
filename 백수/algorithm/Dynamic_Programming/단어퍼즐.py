import re,sys
MAX_INT = sys.maxsize
    
def solution(strs, word):
    strs = set(strs)
    dp = [float('inf')]*(len(word)+1)
    dp[0] = 0
    
    for i in range(len(word)):
        for j in range(1,6):
            if i+1>=j and word[i-j+1:i+1] in strs:
                dp[i+1] = min(dp[i+1-j]+1, dp[i+1])

    if dp[-1] != float('inf'):
        return dp[-1]
    return -1