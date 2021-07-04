def solution(d, budget):
    answer = 0
    tmp = 0
    d.sort()
    for i in d:
        tmp += i
        if tmp > budget:
            break
        else:
            answer += 1
    return answer