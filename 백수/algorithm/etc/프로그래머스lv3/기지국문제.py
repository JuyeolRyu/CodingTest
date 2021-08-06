import math
def solution(n, stations, w):
    answer = 0
    left = 1
    li = []
    for s in stations:
        li.append([left,s-w-1])
        left = s+w+1
    if left <= n:
        li.append([left,n])
    for l in li:
        s,e = l
        answer += math.ceil((e-s+1)/(2*w+1))

    return answer