def solution(c):
    answer = 0
    c = sorted(c,reverse = True)
    h = c[0]
    for h in range(c[0],0,-1):
        for idx in range(len(c)):
            if c[idx] >= h and idx+1>=h and len(c)-idx<=h:
                return h

    return answer