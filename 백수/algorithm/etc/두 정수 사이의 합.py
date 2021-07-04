#https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    answer = 0
    a,b = sorted([a,b])
    for n in range(a,b+1):
        answer += n
    return answer