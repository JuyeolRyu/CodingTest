import math
def solution(N, number):
    answer = -1
    dp = [[]]

    for i in range(1,9):
        tmp = []
        tmp.append(int(i*str(N)))
        for j in range(1,i):
            for n1 in dp[j]:
                for n2 in dp[i-j]:
                    tmp.append(n1+n2)
                    tmp.append(abs(n1-n2))
                    tmp.append(n1*n2)
                    if n2>0:
                        tmp.append(n1//n2)
                        
        if number in tmp:
            return i
        dp.append(tmp)
        
    return answer