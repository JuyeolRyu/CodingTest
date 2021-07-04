#https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        name,parts = c
        if parts in dic:
            dic[parts] += 1
        else:
            dic[parts] = 1
    for parts in dic:
        answer *= (dic[parts]+1)
    return answer-1