def solution(array, commands):
    answer = []
    for s,e,i in commands:
        answer.append(list(sorted(array[s-1:e]))[i-1])
    return answer