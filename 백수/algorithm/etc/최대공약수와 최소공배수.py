def solution(n, m):
    n,m = sorted([n,m])
    answer = [0,0]
    
    for i in range(1,n+1):
        if n%i == 0 and m%i == 0 and answer[0]<i:
            answer[0] = i
    i = n
    while True:
        if i%n == 0 and i%m == 0:
            answer[1] = i
            break
        i+=1
    return answer