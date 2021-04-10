#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    for c in completion:
        if c in dic:
            dic[c] -= 1
    for p in participant:
        if dic[p] > 0:
            answer = p
    return answer