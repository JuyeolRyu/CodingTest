def solution(left, right):
    def divisor(n):
        cnt = 0
        for i in range(1,n+1):
            if n%i == 0:
                cnt += 1
        if cnt%2 == 0:
            return n
        else:
            return -n
    answer = 0
    for n in range(left,right+1):
        answer += divisor(n)
    return answer